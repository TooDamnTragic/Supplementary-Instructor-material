import pyopencl as cl
import numpy as np
import time

# Array size for benchmarking (adjust as needed for your GPU's memory)
array_size = 10**7

# Initialize data for the test
a_np = np.random.rand(array_size).astype(np.float32)
b_np = np.random.rand(array_size).astype(np.float32)

# OpenCL kernel for a simple element-wise addition
kernel_code = """
__kernel void add_arrays(__global const float *a, __global const float *b, __global float *c) {
    int gid = get_global_id(0);
    c[gid] = a[gid] + b[gid];
}
"""

# Iterate over each platform and device to benchmark them
def benchmark_platforms():
    fastest_platform = None
    fastest_device = None
    best_time = float('inf')
    
    for platform in cl.get_platforms():
        print(f"\nTesting Platform: {platform.name}")
        for device in platform.get_devices():
            print(f"  Device: {device.name}")
            
            # Set up OpenCL context and queue
            context = cl.Context([device])
            queue = cl.CommandQueue(context)
            
            # Compile the kernel
            program = cl.Program(context, kernel_code).build()
            
            # Allocate OpenCL buffers
            a_g = cl.Buffer(context, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=a_np)
            b_g = cl.Buffer(context, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=b_np)
            c_g = cl.Buffer(context, cl.mem_flags.WRITE_ONLY, a_np.nbytes)
            
            # Warm-up run to ensure any caching/setup is complete
            program.add_arrays(queue, a_np.shape, None, a_g, b_g, c_g)
            queue.finish()
            
            # Benchmark the kernel execution time
            start_time = time.time()
            program.add_arrays(queue, a_np.shape, None, a_g, b_g, c_g)
            queue.finish()
            elapsed_time = time.time() - start_time
            
            print(f"    Execution time: {elapsed_time:.5f} seconds")
            
            # Check if this is the fastest device
            if elapsed_time < best_time:
                best_time = elapsed_time
                fastest_platform = platform
                fastest_device = device

    print("\n--- Benchmark Results ---")
    if fastest_platform and fastest_device:
        print(f"Fastest Platform: {fastest_platform.name}")
        print(f"Fastest Device: {fastest_device.name}")
        print(f"Best Execution Time: {best_time:.5f} seconds")
    else:
        print("No OpenCL platforms found.")

# Run the benchmark
benchmark_platforms()
