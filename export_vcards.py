import csv
import re
import os

def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename)

def create_vcard(contact):
    vcard_template = f"""BEGIN:VCARD
VERSION:3.0
FN:{contact['Name']}
N:{contact['Family Name']};{contact['Given Name']};{contact['Additional Name']};;{contact['Name Prefix']}
EMAIL;TYPE={contact['E-mail 1 - Type']}:{contact['E-mail 1 - Value']}
TEL;TYPE={contact['Phone 1 - Type']}:{contact['Phone 1 - Value']}
TEL;TYPE={contact['Phone 2 - Type']}:{contact['Phone 2 - Value']}
TEL;TYPE={contact['Phone 3 - Type']}:{contact['Phone 3 - Value']}
ADR;TYPE={contact['Address 1 - Type']}:{contact['Address 1 - PO Box']};{contact['Address 1 - Street']};{contact['Address 1 - City']};{contact['Address 1 - Region']};{contact['Address 1 - Postal Code']};{contact['Address 1 - Country']}
ORG:{contact['Organization 1 - Name']};{contact['Organization 1 - Department']}
TITLE:{contact['Organization 1 - Title']}
END:VCARD
"""
    return vcard_template

def export_contacts_to_vcards(csv_file_path):
    output_folder = 'vcard'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            vcard_content = create_vcard(row)
            sanitized_name = sanitize_filename(row['Name'])
            file_name = f"{sanitized_name}.vcf"
            file_path = os.path.join(output_folder, file_name)
            with open(file_path, 'w', encoding='utf-8') as vcardfile:
                vcardfile.write(vcard_content)
    print("Exportation terminée !")

if __name__ == "__main__":
    csv_file_path = 'contacts.csv'  # Changez ce chemin vers le chemin de votre fichier CSV
    export_contacts_to_vcards(csv_file_path)
