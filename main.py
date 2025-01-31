from docxtpl import DocxTemplate

# Load the template
doc = DocxTemplate("example.docx")

# Create the context with our data
context = {
    'name': 'peter'
}

# Render the template with our context
doc.render(context)

# Save the generated document
doc.save("generated_doc.docx")
