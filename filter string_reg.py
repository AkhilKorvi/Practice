import re

def filter_irp_elements(elements):
    pattern = r'^IRP\d{3}$'  # Regular expression pattern to match "IRP" followed by exactly 3 digits
    filtered_elements = [element for element in elements if re.match(pattern, element)]
    return filtered_elements

# Example usage
elements = ['IRP123', 'IRP456', 'ABC789', 'IRP78', 'IRP001', 'XYZ123', 'IRP000']
result = filter_irp_elements(elements)
print(result)
