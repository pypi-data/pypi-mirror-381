import sys
from pathlib import Path
from tqdm import tqdm

from .ollama import transcribe_image, check_for_server
from .utils import setup_output_dirs, merge_text_files, pdf_to_images, resize_image


def process_pdf(
    pdf_path: str,
    custom_instructions: str,
    output_dir: str,
    model: str,
    keep_images: bool,
    width: int,
    start: int,
    end: int,
    stdout: bool,
    server_url: str,
) -> None:
    """
    Process a PDF file, converting pages to images and transcribing them.

    Args:
        pdf_path (str): The path to the PDF file.
        custom_instructions (str): Additional instructions for the transcription prompt.
        output_dir (str): The directory to save the output.
        model (str): The model to use for transcription.
        keep_images (bool): Whether to keep the images after processing.
        width (int): The width of the resized images.
        start (int): The start page number.
        end (int): The end page number.
        stdout (bool): Whether to write output to stdout.
        server_url (str): The URL of the Ollama server.
    """
    pdf_path = Path(pdf_path)
    output_base = Path(output_dir)

    if not pdf_path.exists():
        print(f"Error: PDF file not found: {pdf_path}")
        sys.exit(1)

    if not check_for_server(server_url):
        print(
            "Error: Ollama server not running. Please start the server and try again."
        )
        sys.exit(1)

    # Read custom instructions file if provided
    custom_instructions_content = None
    if custom_instructions:
        custom_instructions_path = Path(custom_instructions)
        if not custom_instructions_path.exists():
            print(
                f"Error: Custom instructions file not found: {custom_instructions_path}"
            )
            sys.exit(1)
        try:
            with open(custom_instructions_path, "r", encoding="utf-8") as f:
                custom_instructions_content = f.read().strip()
        except Exception as e:
            print(f"Error reading custom instructions file: {str(e)}")
            sys.exit(1)

    # Setup output directories
    image_dir, text_dir = setup_output_dirs(output_base)

    try:
        # Convert PDF to images
        pdf_to_images(str(pdf_path), image_dir, start, end)

        # Process each page
        image_files = sorted(image_dir.glob("page_*.png"))
        total_pages = len(image_files)

        # Resize images to 500px width
        if width > 0:
            for image_file in tqdm(image_files, desc="Resizing images"):
                resize_image(str(image_file), str(image_file), width)
        else:
            pass  # Skip resizing

        for i, image_file in tqdm(
            enumerate(image_files, 1),
            desc="Transcribing pages",
            total=total_pages,
        ):
            # Transcribe the image
            try:
                transcription = transcribe_image(
                    str(image_file),
                    model=model,
                    custom_instructions=custom_instructions_content,
                    server_url=server_url,
                )

                # Save transcription
                text_file = text_dir / f"{image_file.stem}.txt"
                with open(text_file, "w", encoding="utf-8") as f:
                    f.write(transcription)
            except Exception as e:
                print(f"Error processing page {i}: {str(e)}", file=sys.stderr)

            # Clean up image if not keeping them
            if not keep_images:
                image_file.unlink()

        # Merge text files
        merged_file = merge_text_files(text_dir)

        if stdout:
            print(open(merged_file, "r").read(), file=sys.stdout)

        print(f"Processing complete! Output saved to: {output_base}", file=sys.stderr)

    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
