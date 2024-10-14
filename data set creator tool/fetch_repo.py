import requests
import os
import json

def fetch_repo_data(repo_url):
    url = f"https://api.github.com/repos/{repo_url}/contents"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

def clone_repo(repo_url):
    os.system(f'git clone {repo_url}')

def extract_code_snippets(path):
    code_snippets = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(('.kt', '.gradle', '.xml', '.txt', '.md', '.res', '.pro', '.properties', '.json')):  # Tuple of extensions
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:  # Use encoding for better handling of file content
                    content = f.read()
                    code_snippets.append(content)
    return code_snippets

def create_dataset(snippets):
    dataset = []
    for snippet in snippets:
        dataset.append({"input": snippet, "output": "your expected response"})
    return dataset

# Main execution
if __name__ == "__main__":
    owner = 'user_name'  # Replace with your GitHub username
    repo_name = 'repo_name'  # Replace with your GitHub repository name
    repo_url = f'https://github.com/{owner}/{repo_name}.git'
    
    # Clone the repository
    clone_repo(repo_url)
    
    # Extract snippets from the relevant files in the cloned repository
    snippets = extract_code_snippets(repo_name)  # Adjust the path if necessary
    
    # Create dataset from the extracted snippets
    training_data = create_dataset(snippets)

    # Save the dataset to a JSON file
    with open('training_data.json', 'w') as f:
        json.dump(training_data, f, indent=4)  # Added indent for better readability
    print("Dataset created successfully!")
