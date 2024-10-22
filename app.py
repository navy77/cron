import streamlit  as st
import os

# Path to the Ofelia config file
config_path = './config.ini'

def load_config():
    # Load the current config from the file
    if os.path.exists(config_path):
        with open(config_path, 'r') as file:
            return file.read()
    return ''

def save_config(new_config):
    # Save the new config to the file
    with open(config_path, 'w') as file:
        file.write(new_config)

def update_config(schedule, command):
    # Update the config with the new schedule and command
    new_config = f'''
[job-run "Run Python Script"]
schedule = {schedule}
container = python_app
command = {command}
'''
    save_config(new_config)

def restart_ofelia():
    os.system('docker-compose restart ofelia')

# Streamlit interface
st.title("Ofelia Scheduler Configuration")

# Input fields for schedule and command
schedule = st.text_input("Job Schedule (e.g., @every 1m)", "@every 1m")
command = st.text_input("Command to run", "python /app/main.py")

# Button to save the config
if st.button("Update Configuration"):
    update_config(schedule, command)
    st.success("Configuration updated! You may need to restart Ofelia for changes to take effect.")

# Button to restart Ofelia
if st.button("Restart Ofelia"):
    restart_ofelia()
    st.success("Ofelia restarted successfully!")

# Show the current config
st.subheader("Current Configuration")
current_config = load_config()
st.text_area("Config File", current_config, height=200)
