# import os
# import re

# from django.apps import apps

# def project_analysis():

#     # Get all installed apps
#     installed_apps = apps.get_app_configs()

#     for values in installed_apps:
#         print(values.name)

#     # Count the number of apps
#     num_apps = len(installed_apps)

#     print(f"\nNumber of Apps: {num_apps}\n\n")

#     # models
#     # Count the total number of models and print model names
#     total_models = 0
#     for space in installed_apps:
#         # Get all models for the current app
#         model = space.get_models()
#         space_list = list(model)  # Convert generator to list
#         models_in_space = len(space_list)  # Count the number of models
#         total_models += models_in_space
        
#         # Print model names
#         for model in space_list:
#             print(f"- {model.__name__}")

#     print(f"Total Number of Models: {total_models}")

#     # views
#     # Define the base directory of your project
#     project_dir = os.path.dirname(os.path.dirname(__file__))

#     # List to store identified view names
#     view_names = []
#     # Regular expression for views (can be improved)
#     view_pattern = r"\s*def\s+(.+?)\(.*?\):\s*@\s*view_config"

#     # Count total views and functions
#     total_views = 0
#     total_functions = 0

#     # Iterate through each app directory
#     for app_dir in [d for d in os.listdir(project_dir) if os.path.isdir(os.path.join(project_dir, d)) and not d.startswith('.')]:
#         # Define the views module path
#         views_path = os.path.join(project_dir, app_dir, 'views.py')

#     # Check if views.py exists
#     if os.path.exists(views_path):
#         # Open the views.py file and read its contents
#         with open(views_path, 'r') as f:
#             file_content = f.read()

#         # Search for views using the regular expression
#         matches = re.findall(view_pattern, file_content, re.MULTILINE)

#         # Extract view names from matches
#         for match in matches:
#             # Assuming the first capturing group captures the view name
#             view_name = match.strip()  # Remove extra whitespaces
#             view_names.append(view_name)
#         # You can define specific patterns to identify views and functions (e.g., looking for def statements with decorators like @view_config)
#         # Here's a simplified example (might need adjustments):
#         total_views += file_content.count("def ")  # Count occurrences of def (might include non-view functions)
#         total_functions += file_content.count("def ")  # Same as above (can be improved)
    
#     # Print the identified view names
#     print("Identified View Names:")
#     for view_name in view_names:
#         print(f"- {view_name}")
    
#     # Print the results
#     print(f"Number of Views (Approx): {total_views}")
#     print(f"Number of Functions (Approx): {total_functions}")