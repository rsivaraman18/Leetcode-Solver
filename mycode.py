import os
import subprocess
import time

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

def main():
    while True:
        # Check the status of the Git repository
        result = run_command(commands['status'])
        status_output = result.stdout.strip()
        
        if status_output:
            # Get the first untracked or modified file
            files = [line.split()[1] for line in status_output.splitlines()]
            if files:
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
        
        # Wait for 1 minute before checking the status again
        time.sleep(60)

if __name__ == "__main__":
    main()


