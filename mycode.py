import subprocess
import time
import re

# Define the Git commands
commands = {
    'status': 'git status --porcelain',
    'add': 'git add {filename}',
    'commit': 'git commit -m "Program Solved"',
    'push': 'git push origin main'
}

def run_command(command, filename=None):
    if filename:
        command = command.format(filename=filename)
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result

def parse_git_status(status_output):
    # Use regex to match file paths, including those with spaces
    pattern = r'^[ MADRCU?]{1,2} (.+)$'
    return re.findall(pattern, status_output, re.MULTILINE)

def main():
    while True:
        # Check the status of the Git repository
        result = run_command(commands['status'])
        status_output = result.stdout.strip()
        
        if status_output:
            # Parse the status output to get the list of files
            files = parse_git_status(status_output)
            if files:
                # Print the list of files
                print(f'Files detected for status update: {files}')
                
                # Process the first file
                filename = files[0]
                
                # Add the file
                run_command(commands['add'], filename)
                
                # Commit the changes
                run_command(commands['commit'])
                
                # Push the changes
                push_result = run_command(commands['push'])
                if push_result.returncode == 0:
                    print(f'Successfully pushed the file: {filename}')
                else:
                    print(f'Failed to push the file: {filename}')
                    print(push_result.stderr)
        
            waiting_time = 300
            print('Now I will be waiting for {waiting_time} seconds')
            time.sleep(waiting_time)
        else:
            rest_time = 900
            print('No Untracked or Modified Files Found. So Let me take Rest for ', int(rest_time)/60 ,'minutes')
            time.sleep(rest_time) 


if __name__ == "__main__":
    main()
