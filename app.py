import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to create a PDF with ReportLab
def generate_pdf(name, address, mobile, groceries):
    pdf_output = "/mnt/data/grocery_list_reportlab.pdf"
    c = canvas.Canvas(pdf_output, pagesize=letter)
    
    # Add title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 750, "Grocery List")

    # Add Name, Address, and Mobile
    c.setFont("Helvetica", 12)
    c.drawString(100, 700, f"Name: {name}")
    c.drawString(100, 680, f"Address: {address}")
    c.drawString(100, 660, f"Mobile: {mobile}")

    # Add Groceries List
    c.drawString(100, 630, "Groceries to Buy:")
    y_position = 610
    for grocery in groceries:
        c.drawString(100, y_position, f"- {grocery}")
        y_position -= 20

    # Save PDF
    c.save()
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
                    file_name="grocery_list_reportlab.pdf",
                    mime="application/pdf"
                )
            else:
                st.error("Please fill out all fields.")

if __name__ == "__main__":
    main()
