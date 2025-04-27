import streamlit as st
from fpdf import FPDF

# Function to create a PDF from collected data
def generate_pdf(name, address, mobile, groceries):
    # Create a PDF object
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Set title and font
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Grocery List", ln=True, align='C')

    # Add Name
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)

    # Add Address
    pdf.cell(200, 10, txt=f"Address: {address}", ln=True)

    # Add Mobile Number
    pdf.cell(200, 10, txt=f"Mobile: {mobile}", ln=True)

    # Add Groceries List
    pdf.ln(10)
    pdf.cell(200, 10, txt="Groceries to Buy:", ln=True)
    for grocery in groceries:
        pdf.cell(200, 10, txt=f"- {grocery}", ln=True)

    # Save PDF to file
    pdf_output = "/mnt/data/grocery_list.pdf"
    pdf.output(pdf_output)

    return pdf_output

# Streamlit UI for collecting data
def main():
    st.title("Grocery List Form")

    # Collect user inputs using text input and multiselect
    with st.form(key='grocery_form'):
        # User inputs
        name = st.text_input("Enter your Name:")
        address = st.text_area("Enter your Address:")
        mobile = st.text_input("Enter your Mobile Number:")
        groceries = st.multiselect("Select Groceries to Buy:", 
                                    ["Apples", "Bananas", "Carrots", "Eggs", "Milk", "Bread", "Rice", "Cheese", "Tomatoes"])

        # Submit button
        submit_button = st.form_submit_button("Generate PDF")

        if submit_button:
            if name and address and mobile and groceries:
                # Generate PDF if all fields are filled
                pdf_file = generate_pdf(name, address, mobile, groceries)

                # Provide a download link for the generated PDF
                st.success("PDF generated successfully!")
                st.download_button(
                    label="Download Grocery List PDF",
                    data=open(pdf_file, "rb").read(),
                    file_name="grocery_list.pdf",
                    mime="application/pdf"
                )
            else:
                st.error("Please fill out all fields.")

if __name__ == "__main__":
    main()
