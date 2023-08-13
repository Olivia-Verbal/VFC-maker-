def create_vcard(name, phone):
    vcard = f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nTEL:{phone}\nEND:VCARD\n"
    return vcard

def save_vcards(filename, vcards):
    with open(filename, 'w') as f:
        for vcard in vcards:
            f.write(vcard)

def main():
    input_filename = input("Enter the input text file name (e.g., some contacts.txt): ")
    output_filename = input("Enter the vCard output file name (e.g., some contacts.vcf): ")
    vcards = []

    try:
        with open(input_filename, 'r') as f:
            lines = f.readlines()

        i = 0
        while i < len(lines):
            name = lines[i].strip()
            phone = lines[i + 1].strip()
            vcard = create_vcard(name, phone)
            vcards.append(vcard)
            i += 3  # Skip the blank line between entries

        save_vcards(output_filename, vcards)
        print(f"{len(vcards)} vCards saved to {output_filename}")
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")

if __name__ == "__main__":
    main()
