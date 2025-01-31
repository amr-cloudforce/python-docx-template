from docxtpl import DocxTemplate

# Load the template
doc = DocxTemplate("example.docx")

# Create the context with our data
context = {
    'name': 'Peter',
    'jobs': [
        {
            'date_from': 'Mai 2012',
            'date_to': 'Januar 2017',
            'company': 'Musterladen GmbH',
            'role': 'Tätigkeit als Projektmanager und Qualitätsverantwortlicher',
            'tasks': [
                'Einführung ISO 17020',
                'Beschleunigung der Beschaffungsprozesse',
                'Verbesserung der Kundenprozesse'
            ]
        },
        {
            # Second job entry
            'date_from': 'Mai 2008',
            'date_to': 'April 2012',
            'company': 'SEOXPERT AG',
            'role': 'Tätigkeit als Senior Projektmanager',
            'tasks': [
                'Grössere Kundenprojekte im Bereich eMarketing',
                'Einführung div. Qualitätsmanagement-Systeme'
            ]
        }
        # Add more jobs as needed
    ]
}

# Render the template with our context
doc.render(context)

# Save the generated document
doc.save("generated_doc.docx")
