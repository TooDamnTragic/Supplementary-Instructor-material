import subprocess
import pyopencl as cl
import numpy as np
import string
import threading

# Path to the image file
image_file = "Victor.jpg"

# Character set to use in brute-force (letters, numbers, underscore, dash)
charset = string.ascii_letters + string.digits + "_-"
charset_array = np.array([ord(c) for c in charset], dtype=np.uint8)

# Configure batch size to generate larger workloads per GPU call
batch_size = 10000  # Adjust based on GPU capabilities
max_length = 10     # Maximum password length

# Kernel to generate password candidates on the GPU
kernel_code = """
__kernel void generate_passwords(
    __global const char *charset,
    __global char *output,
    const unsigned int charset_len,
    const unsigned int length,
    const unsigned int batch_start
) {
    int idx = get_global_id(0) + batch_start;
    int pos = idx;

    for (int i = 0; i < length; i++) {
        output[(idx - batch_start) * length + i] = charset[pos % charset_len];
        pos /= charset_len;
    }
}
"""

# Function to select the NVIDIA CUDA platform and NVIDIA GPU device
def get_nvidia_cuda_context():
    # Select the NVIDIA CUDA platform
    for platform in cl.get_platforms():
        if "NVIDIA CUDA" in platform.name:
            # Choose the NVIDIA GeForce RTX 4080 Laptop GPU device
            for device in platform.get_devices():
                if "NVIDIA GeForce RTX 4080" in device.name:
                    return cl.Context([device])

    raise RuntimeError("NVIDIA CUDA platform with NVIDIA GeForce RTX 4080 not found.")

# Set up OpenCL context and command queue
context = get_nvidia_cuda_context()
queue = cl.CommandQueue(context)

# Compile kernel code
program = cl.Program(context, kernel_code).build()

# Function to run steghide in a separate thread
def try_password(password, found_event, attempt_counter):
    if found_event.is_set():  # Stop other threads if password is found
        return
    try:
        # Run the steghide extract command with each password
        result = subprocess.run(
            ["steghide.exe", "extract", "-sf", image_file, "-p", password],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True
        )

        # Check if extraction was successful
        if "wrote extracted data" in result.stdout:
            print(f"[+] Password found: {password}")
            found_event.set()  # Signal other threads to stop
    except Exception as e:
        print(f"Error with password '{password}': {e}")

    # Increment and print progress every 1000 attempts
    attempt_counter[0] += 1
    if attempt_counter[0] % 1000 == 0:
        print(f"Attempted {attempt_counter[0]} passwords so far...")

# Function to brute-force steghide with GPU-generated passwords
def brute_force_steghide(image, max_length=10):
    found_event = threading.Event()  # Event to stop threads when password is found
    attempt_counter = [0]  # Mutable counter to track attempts across threads

    for length in range(5, max_length + 1):
        print(f"[*] Trying passwords of length {length}...")

        # Calculate total combinations for current length
        total_combinations = len(charset) ** length
        batch_start = 0

        while batch_start < total_combinations and not found_event.is_set():
            # Allocate buffer for a batch of passwords
            output_buffer = np.empty((batch_size, length), dtype=np.uint8)

            # Create OpenCL buffers
            charset_buffer = cl.Buffer(context, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=charset_array)
            output_buffer_opencl = cl.Buffer(context, cl.mem_flags.WRITE_ONLY, output_buffer.nbytes)

            # Run kernel to generate a batch of password combinations
            program.generate_passwords(
                queue, (batch_size,), None,
                charset_buffer,
                output_buffer_opencl,
                np.uint32(len(charset)),
                np.uint32(length),
                np.uint32(batch_start)
            )
            cl.enqueue_copy(queue, output_buffer, output_buffer_opencl).wait()

            # Convert generated passwords and launch threads
            threads = []
            for password_array in output_buffer:
                password = ''.join(map(chr, password_array)).strip('\x00')
                t = threading.Thread(target=try_password, args=(password, found_event, attempt_counter))
                t.start()
                threads.append(t)

            # Wait for all threads to complete
            for t in threads:
                t.join()

            # Move to the next batch
            batch_start += batch_size

            # Check if password was found to break the loop
            if found_event.is_set():
                return

    print("[-] No password found within the specified length.")

# Run the brute-force function with a specified max length
brute_force_steghide(image_file, max_length=max_length)
