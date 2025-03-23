import pikepdf
import re

def analyze_pdf(file_path):
    try:
        # Open the PDF
        pdf = pikepdf.Pdf.open(file_path)
        print("PDF Version:", pdf.pdf_version)
        print("Number of pages:", len(pdf.pages))
        print("Metadata:")
        for key, value in pdf.docinfo.items():
            print(f"  {key}: {value}")
        
        # Check for embedded files in the PDF trailer
        print("\nChecking for embedded files:")
        embedded_found = False
        if "/Names" in pdf.trailer:
            names = pdf.trailer["/Names"]
            if "/EmbeddedFiles" in names:
                ef = names["/EmbeddedFiles"]
                if "/Names" in ef:
                    embedded_files = ef["/Names"]
                    # The embedded files are stored as [name1, file_spec1, name2, file_spec2, ...]
                    for i in range(0, len(embedded_files), 2):
                        file_name = embedded_files[i]
                        file_spec = embedded_files[i+1]
                        print("Found embedded file:", file_name)
                        embedded_found = True
                        # Optionally extract the file if needed:
                        if "/EF" in file_spec:
                            ef_dict = file_spec["/EF"]
                            if "/F" in ef_dict:
                                file_stream = ef_dict["/F"]
                                extracted_file = file_name
                                with open(extracted_file, "wb") as out_f:
                                    out_f.write(file_stream.read_bytes())
                                print(f"Extracted file saved as: {extracted_file}")
        if not embedded_found:
            print("No embedded files found.")
            
        # Check for potential JavaScript actions
        print("\nScanning for JavaScript actions in the PDF:")
        # Loop through the indirect objects
        js_found = False
        for obj in pdf.objects:
            try:
                obj_str = str(obj)
                if "/JavaScript" in obj_str:
                    print("Suspicious JavaScript found in object:")
                    print(obj_str)
                    js_found = True
            except Exception as inner_err:
                continue
        if not js_found:
            print("No JavaScript actions found.")
            
    except Exception as e:
        print("Error processing PDF:", e)

def search_for_flag(file_path):
    # Read the file in binary and search for the flag pattern
    with open(file_path, "rb") as f:
        data = f.read()
    # Use a non-greedy search for the flag format
    flags = re.findall(b"MetaCTF\{.*?\}", data)
    if flags:
        print("\nPotential flags found in raw data:")
        for flag in flags:
            print(flag.decode('utf-8'))
    else:
        print("\nNo flag found in the raw PDF bytes.")

if __name__ == '__main__':
    file_path = "SI/report.pdf"
    print("=== Analyzing PDF Structure ===")
    analyze_pdf(file_path)
    print("\n=== Searching for Hidden Flag ===")
    search_for_flag(file_path)
