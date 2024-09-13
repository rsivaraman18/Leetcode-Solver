import os
import subprocess
import time

# Define the Git commands
commands = {
    'status': 'git status --porcelain',
    'add': 'git add .',
    'commit': 'git commit -m "Program Solved"',
    'push': 'git push origin main'
}

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result

def main():
    while True:
        # Check the status of the Git repository
        result = run_command(commands['status'])
        status_output = result.stdout.strip()
        
        if status_output:
            # Add all changes (including new files and folders)
            run_command(commands['add'])
            
            # Commit the changes
            commit_result = run_command(commands['commit'])
            if commit_result.returncode == 0:
                # Push the changes
                push_result = run_command(commands['push'])
                if push_result.returncode == 0:
                    print('Successfully pushed the changes.')
                else:
                    print('Failed to push the changes.')
                    print(push_result.stderr)
            else:
                print('Failed to commit changes.')
                print(commit_result.stderr)
        else:
            print('No file to commit,so lets sleep for 30 minutes')
            # Wait for 30 minutes before checking the status again
            time.sleep(1800)
            continue
        
        # Wait for 1 minute before checking the status again
        time.sleep(60)

if __name__ == "__main__":
    main()
