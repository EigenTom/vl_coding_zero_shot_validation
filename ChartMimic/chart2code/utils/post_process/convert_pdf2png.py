# from pdf2image import convert_from_path
# from argparse import ArgumentParser
# import os
# from dotenv import load_dotenv
# from tqdm import tqdm
# from multiprocessing import Pool, cpu_count

# load_dotenv()

# def convert_single_page_pdf_to_png(pdf_path):
#     png_path = pdf_path.replace(".pdf", ".png")
#     try:
#         print(f"Converting {pdf_path} to {png_path}")
#         images = convert_from_path(pdf_path, dpi=120)
#         images[0].save(png_path, "PNG")
#     except Exception as e:
#         print(f"Failed to convert {pdf_path} to {png_path}: {e}")
#         # Handle the case where conversion fails
#         os.system(f"cp {os.environ['PROJECT_PATH']}/assets/blank.png {png_path}")

# def process_pdf(pdf_file, dir_path):
#     pdf_path = os.path.join(dir_path, pdf_file)
#     convert_single_page_pdf_to_png(pdf_path)

# if __name__ == "__main__":
#     parser = ArgumentParser()
#     parser.add_argument("--dir_path", type=str, required=True)

#     args = parser.parse_args()

#     print(f"Converting PDFs to PNGs for all PDFs in {args.dir_path}")

#     pdf_files = [f for f in os.listdir(args.dir_path) if f.endswith(".pdf")]

#     # Create a pool of processes
#     num_processes = cpu_count()  # Use the number of CPU cores available
#     with Pool(processes=num_processes) as pool:
#         list(tqdm(pool.imap(lambda pdf_file: process_pdf(pdf_file, args.dir_path), pdf_files), total=len(pdf_files), desc="Processing PDFs"))
#     # for pdf_file in tqdm(pdf_files):
#     #     pdf_path = os.path.join(args.dir_path, pdf_file)
#     #     png_path = pdf_path.replace(".pdf", ".png")
        
#     #     try:
#     #         print(pdf_path)
#     #         convert_single_page_pdf_to_png(pdf_path, png_path)
#     #     except:
#     #         print(f"Failed to convert {pdf_path} to {png_path}")
#     #         os.system(f"cp {os.environ['PROJECT_PATH']}/assets/blank.png  {png_path}")          

#     code_files = [f for f in os.listdir(f"{os.environ['PROJECT_PATH']}/dataset/enhance_2500") if f.endswith("py")]
#     for code_file in code_files:
#         code_path = os.path.join(args.dir_path, code_file)
#         pdf_path = code_path.replace(".py", ".pdf")
#         png_path = code_path.replace(".py", ".png")
#         if not os.path.exists(pdf_path):
#             os.system(f"cp {os.environ['PROJECT_PATH']}/assets/blank.pdf  {pdf_path}")
#             os.system(f"cp {os.environ['PROJECT_PATH']}/assets/blank.png  {png_path}")

from pdf2image import convert_from_path
from argparse import ArgumentParser
import os
from dotenv import load_dotenv
from tqdm import tqdm
from multiprocessing import Process

load_dotenv()

def convert_single_page_pdf_to_png(pdf_path, output_path, dpi=120):
    images = convert_from_path(pdf_path, dpi=dpi)
    images[0].save(output_path, "PNG")

def _muti_process_run(rank, pdf_files, dir_path, num_processes):
    sub_index = [_ for _ in range(len(pdf_files))][rank :: num_processes]

    for i in tqdm(sub_index, disable=rank != 0):
        pdf_file = pdf_files[i]
        pdf_path = os.path.join(dir_path, pdf_file)
        png_path = pdf_path.replace(".pdf", ".png")
        
        try:
            print(pdf_path)
            convert_single_page_pdf_to_png(pdf_path, png_path)
        except Exception as e:
            print(f"Failed to convert {pdf_path} to {png_path}: {e}")
            os.system(f"cp {os.environ['PROJECT_PATH']}/assets/blank.png {png_path}")

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--dir_path", type=str, required=True)

    args = parser.parse_args()

    print(f"Converting PDFs to PNGs for all PDFs in {args.dir_path}")

    pdf_files = [f for f in os.listdir(args.dir_path) if f.endswith(".pdf")]

    processes = []
    num_processes = 20
    for rank in range(num_processes):
        p = Process(target=_muti_process_run, args=(rank, pdf_files, args.dir_path, num_processes))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()

    print("PDF to PNG conversion completed.")

    code_files = [f for f in os.listdir(f"{os.environ['PROJECT_PATH']}/dataset/direct_2400") if f.endswith("py")]
    for code_file in code_files:
        code_path = os.path.join(args.dir_path, code_file)
        pdf_path = code_path.replace(".py", ".pdf")
        png_path = code_path.replace(".py", ".png")
        if not os.path.exists(pdf_path):
            print(f"pad blank.pdf to {pdf_path}")
            os.system(f"cp {os.environ['PROJECT_PATH']}/assets/blank.pdf {pdf_path}")
            os.system(f"cp {os.environ['PROJECT_PATH']}/assets/blank.png {png_path}")
