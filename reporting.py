import jinja2
import json

def generate_report(data, template_path, output_path):
    with open(template_path) as file:
        template = jinja2.Template(file.read())
    
    report_content = template.render(data=data)
    
    with open(output_path, 'w') as report_file:
        report_file.write(report_content)

# Example usage
if __name__ == "__main__":
    sample_data = {
        "files": [
            {"name": "example.txt", "size": 1024, "created": "2024-01-01"},
            {"name": "image.jpg", "size": 2048, "created": "2024-02-01"}
        ]
    }
    generate_report(sample_data, 'report_template.html', 'report.html')
