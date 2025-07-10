#!/usr/bin/env python3
"""
vm_manager.py

Author: Michael B.
Date: 9 April 2025
"""

import subprocess
import sys
import logging
import os

# Logging
LOG_FILE = "vm_manager.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_command(command_list):
    #Helper function to run commands using subprocess
    
    try:
        result = subprocess.run(command_list,capture_output=True,text=True,check=False)
        return (result.returncode, result.stdout.strip(), result.stderr.strip())
    except FileNotFoundError:
        return (1, "", f"Command not found: {command_list[0]}")
    except Exception as e:
        return (1, "", f"Unexpected error: {str(e)}")


def list_all_vms():
    #list_all_vms
    cmd = ["VBoxManage", "list", "vms"]
    DidItWork, output, error = run_command(cmd)

    if DidItWork != 0:
        print(f"Error listing VMs: {error}")
        logging.error(f"Error listing VMs: {error}")
        return {}

    vm_info_lines = output.splitlines()
    vms = {}
    for line in vm_info_lines:
        # lines look like:  "Win10" {f1234567-89ab-cdef-0123-456789abcdef}
        if line.strip():
            parts = line.split()
            name = line.split('"')[1]
            uuid = parts[-1].strip("{}")
            vms[name] = uuid

    return vms


def list_running_vms():
    #List all RUNNING VMs
    
    cmd = ["VBoxManage", "list", "runningvms"]
    DidItWork, output, error = run_command(cmd)

    if DidItWork != 0:
        print(f"Error listing Running VMs: {error}")
        logging.error(f"Error listing Running VMs: {error}")
        return {}

    vm_info_lines = output.splitlines()
    vms = {}
    for line in vm_info_lines:
        if line.strip():
            parts = line.split()
            name = line.split('"')[1]
            uuid = parts[-1].strip("{}")
            vms[name] = uuid

    return vms


# MENU STUFF

def menu_list_vms():
    #prints all VMs
    
    print("\n=== All Virtual Machines ===")
    all_vms = list_all_vms()
    if not all_vms:
        print("No VMs found.")
        return
    else:
        for i, (name, uuid) in enumerate(all_vms.items(), start=1):
            print(f"{i}. {name} [{uuid}]")
    print("============================")


def menu_start_vm():
    #lets user select a VM from the list and start it
    
    all_vms = list_all_vms()
    if not all_vms:
        print("No VMs to start.")
        return

    print("\n=== Start a VM ===")
    vms_list = list(all_vms.keys())
    for id, vm_name in enumerate(vms_list, start=1):
        print(f"{id}. {vm_name}")
    choice = input("Select a VM to start by number (or 'c' to cancel): ")
    if choice.lower().strip() == 'c':
        return

    try:
        choice_num = int(choice.strip()) - 1
        if choice_num < 0 or choice_num >= len(vms_list):
            print("Invalid selection.")
            return
        vm_to_start = vms_list[choice_num]
    except ValueError:
        print("Invalid input.")
        return

    running_vms = list_running_vms()
    if vm_to_start in running_vms:
        print(f"VM '{vm_to_start}' is already running.")
        logging.warning(f"Attempted to start already running VM '{vm_to_start}'")
        return

    #This command to a while to figure out, couldn't find a smaller way to do this
    cmd = ["VBoxManage", "startvm", vm_to_start, "--type", "headless"]
    DidItWork, output, error = run_command(cmd)

    if DidItWork != 0:
        print(f"Error starting VM '{vm_to_start}' : {error}")
        logging.error(f"Error starting VM '{vm_to_start}' : {error}")
    else:
        print(f"VM '{vm_to_start}' started successfully.")
        logging.info(f"VM '{vm_to_start}' started.")


def menu_stop_vm():
    #lets user select a VM from the list and stop it
    
    all_r_vms = list_running_vms()
    if not all_r_vms:
        print("No VMs are currently running.")
        return
    
    print("\n=== Stop a VM ===")
    vms_list = list(all_r_vms.keys())
    for id, vm_name in enumerate(vms_list, start=1):
        print(f"{id}. {vm_name}")

    choice = input("Select a VM to stop by number (or 'c' to cancel): ")
    if choice.lower().strip() == 'c':
        return

    try:
        choice_num = int(choice.strip()) - 1
        if choice_num < 0 or choice_num >= len(vms_list):
            print("Invalid selection.")
            return
        vm_to_stop = vms_list[choice_num]
    except ValueError:
        print("Invalid input.")
        return

    # "acpipowerbutton" pretty much presses the power button so I just used this
    cmd = ["VBoxManage", "controlvm", vm_to_stop, "acpipowerbutton"]
    DidItWork, output, error = run_command(cmd)

    if DidItWork != 0:
        print(f"Error stopping VM '{vm_to_stop}' : {error}")
        logging.error(f"Error stopping VM '{vm_to_stop}' : {error}")
    else:
        print(f"Stopping VM '{vm_to_stop}' ...")
        logging.info(f"VM '{vm_to_stop}' stopped.")
    

def menu_create_vm():
    """
    To create a VM, this function:
    - Asks for VM name
    - Asks for memory size
    - Creates a VM, registers it, sets OS type
    - Creates a virtual disk
    """
    print("\n=== Create a New VM ===")
    vm_name = input("Enter VM Name: ").strip()
    if not vm_name:
        print("VM Name cannot be empty.")
        return

    mem_size = input("Enter memory size in MB (e.g., 1024): ").strip()
    if not mem_size.isdigit():
        print("Invalid memory size.")
        return

    disk_size = input("Enter virtual disk size in MB (e.g., 10240): ").strip()
    if not disk_size.isdigit():
        print("Invalid disk size.")
        return

    # 1. Create the VM
    cmd_create_vm = ["VBoxManage", "createvm", "--name", vm_name, "--register"]
    retcode, stdout, stderr = run_command(cmd_create_vm)
    if retcode != 0:
        print(f"Error creating VM: {stderr}")
        logging.error(f"Error creating VM '{vm_name}': {stderr}")
        return

    # 2. Modify VM memory (and optionally OS type, CPU, etc.)
    cmd_modify_vm = [
        "VBoxManage", "modifyvm", vm_name,
        "--memory", mem_size,
        "--ostype", "Other",
        "--cpus", "1"
    ]
    retcode, stdout, stderr = run_command(cmd_modify_vm)
    if retcode != 0:
        print(f"Error modifying VM settings: {stderr}")
        logging.error(f"Error modifying VM '{vm_name}': {stderr}")
        return

    # 3. Create a virtual disk
    disk_path = f"{vm_name}.vdi"
    cmd_create_disk = [
        "VBoxManage", "createhd",
        "--filename", disk_path,
        "--size", disk_size
    ]
    retcode, stdout, stderr = run_command(cmd_create_disk)
    if retcode != 0:
        print(f"Error creating virtual disk: {stderr}")
        logging.error(f"Error creating disk for VM '{vm_name}': {stderr}")
        return

    # 4. Attach storage controller
    cmd_storage_ctl = [
        "VBoxManage", "storagectl", vm_name,
        "--name", "SATA Controller",
        "--add", "sata",
        "--controller", "IntelAhci"
    ]
    retcode, stdout, stderr = run_command(cmd_storage_ctl)
    if retcode != 0:
        print(f"Error creating storage controller: {stderr}")
        logging.error(f"Error creating storage controller for '{vm_name}': {stderr}")
        return

    # 5. Attach the disk to the VM
    cmd_storage_attach = [
        "VBoxManage", "storageattach", vm_name,
        "--storagectl", "SATA Controller",
        "--port", "0",
        "--device", "0",
        "--type", "hdd",
        "--medium", disk_path
    ]
    retcode, stdout, stderr = run_command(cmd_storage_attach)
    if retcode != 0:
        print(f"Error attaching disk to VM: {stderr}")
        logging.error(f"Error attaching disk to '{vm_name}': {stderr}")
        return

    print(f"VM '{vm_name}' created and configured successfully!")
    logging.info(f"VM '{vm_name}' created with {mem_size} MB RAM and {disk_size} MB disk.")


def menu_delete_vm():
    """
    Delete a VM with confirmation.
    """
    all_vms = list_vms()
    if not all_vms:
        print("No VMs to delete.")
        return

    print("\n=== Delete a VM ===")
    vms_list = list(all_vms.keys())
    for idx, vm_name in enumerate(vms_list, start=1):
        print(f"{idx}. {vm_name}")

    choice = input("Select a VM to delete by number (or 'c' to cancel): ")
    if choice.lower() == 'c':
        return

    try:
        choice_idx = int(choice) - 1
        if choice_idx < 0 or choice_idx >= len(vms_list):
            print("Invalid selection.")
            return
        vm_to_delete = vms_list[choice_idx]
    except ValueError:
        print("Invalid input.")
        return

    confirm = input(f"Are you sure you want to delete VM '{vm_to_delete}'? (yes/no): ")
    if confirm.lower() != 'yes':
        print("Delete cancelled.")
        return

    cmd = ["VBoxManage", "unregistervm", vm_to_delete, "--delete"]
    retcode, stdout, stderr = run_command(cmd)
    if retcode != 0:
        print(f"Error deleting VM: {stderr}")
        logging.error(f"Error deleting VM '{vm_to_delete}': {stderr}")
    else:
        print(f"VM '{vm_to_delete}' deleted successfully.")
        logging.info(f"VM '{vm_to_delete}' deleted.")


def menu_vm_settings():
    """
    Allows user to select a VM and then displays its hardware configuration.
    """
    all_vms = list_vms()
    if not all_vms:
        print("No VMs to show settings for.")
        return

    print("\n=== View VM Settings ===")
    vms_list = list(all_vms.keys())
    for idx, vm_name in enumerate(vms_list, start=1):
        print(f"{idx}. {vm_name}")

    choice = input("Select a VM to view settings (or 'c' to cancel): ")
    if choice.lower() == 'c':
        return

    try:
        choice_idx = int(choice) - 1
        if choice_idx < 0 or choice_idx >= len(vms_list):
            print("Invalid selection.")
            return
        vm_to_show = vms_list[choice_idx]
    except ValueError:
        print("Invalid input.")
        return

    cmd = ["VBoxManage", "showvminfo", vm_to_show]
    retcode, stdout, stderr = run_command(cmd)
    if retcode != 0:
        print(f"Error showing VM info: {stderr}")
        logging.error(f"Error showing VM info for '{vm_to_show}': {stderr}")
        return

    print(f"\n=== VM Info for '{vm_to_show}' ===")
    print(stdout)
    print("==============================")


def menu_snapshot_management():
    """
    Manage VM snapshots: take, list, restore.
    """
    print("\n=== Manage VM Snapshots ===")
    all_vms = list_vms()
    if not all_vms:
        print("No VMs available.")
        return

    vms_list = list(all_vms.keys())
    for idx, vm_name in enumerate(vms_list, start=1):
        print(f"{idx}. {vm_name}")

    choice = input("Select a VM by number (or 'c' to cancel): ")
    if choice.lower() == 'c':
        return

    try:
        choice_idx = int(choice) - 1
        if choice_idx < 0 or choice_idx >= len(vms_list):
            print("Invalid selection.")
            return
        vm_selected = vms_list[choice_idx]
    except ValueError:
        print("Invalid input.")
        return

    # Snapshot sub-menu
    while True:
        print(f"\nSnapshot Management for '{vm_selected}'")
        print("1. Take Snapshot")
        print("2. List Snapshots")
        print("3. Restore Snapshot")
        print("4. Back to Main Menu")

        sub_choice = input("Select an option: ").strip()
        if sub_choice == '1':
            snap_name = input("Enter Snapshot Name: ").strip()
            if snap_name:
                cmd = ["VBoxManage", "snapshot", vm_selected, "take", snap_name]
                retcode, stdout, stderr = run_command(cmd)
                if retcode != 0:
                    print(f"Error taking snapshot: {stderr}")
                    logging.error(f"Error taking snapshot '{snap_name}' for VM '{vm_selected}': {stderr}")
                else:
                    print(f"Snapshot '{snap_name}' created for VM '{vm_selected}'.")
                    logging.info(f"Snapshot '{snap_name}' taken for VM '{vm_selected}'.")
            else:
                print("Snapshot name cannot be empty.")

        elif sub_choice == '2':
            # List snapshots
            cmd = ["VBoxManage", "snapshot", vm_selected, "list"]
            retcode, stdout, stderr = run_command(cmd)
            if retcode != 0:
                print(f"Error listing snapshots: {stderr}")
                logging.error(f"Error listing snapshots for VM '{vm_selected}': {stderr}")
            else:
                print(f"\nSnapshots for VM '{vm_selected}':\n{stdout}")

        elif sub_choice == '3':
            snap_name = input("Enter Snapshot Name to restore: ").strip()
            if snap_name:
                cmd = ["VBoxManage", "snapshot", vm_selected, "restore", snap_name]
                retcode, stdout, stderr = run_command(cmd)
                if retcode != 0:
                    print(f"Error restoring snapshot: {stderr}")
                    logging.error(f"Error restoring snapshot '{snap_name}' for VM '{vm_selected}': {stderr}")
                else:
                    print(f"Snapshot '{snap_name}' restored for VM '{vm_selected}'.")
                    logging.info(f"Snapshot '{snap_name}' restored for VM '{vm_selected}'.")
            else:
                print("Snapshot name cannot be empty.")

        elif sub_choice == '4':
            return
        else:
            print("Invalid option. Please try again.")


# ------------------------------------------------------------------------------
# MAIN MENU LOOP
# ------------------------------------------------------------------------------

def main_menu():
    """
    Display the main menu and handle user input.
    """
    while True:
        print("\n===== VirtualBox VM Manager =====")
        print("1. List VMs")
        print("2. Start a VM")
        print("3. Stop a VM")
        print("4. Create a VM")
        print("5. Delete a VM")
        print("6. View VM Settings")
        print("7. Manage VM Snapshots")
        print("0. Exit")
        choice = input("Select an option: ").strip()

        if choice == '1':
            menu_list_vms()
        elif choice == '2':
            menu_start_vm()
        elif choice == '3':
            menu_stop_vm()
        elif choice == '4':
            menu_create_vm()
        elif choice == '5':
            menu_delete_vm()
        elif choice == '6':
            menu_vm_settings()
        elif choice == '7':
            menu_snapshot_management()
        elif choice == '0':
            print("Exiting VirtualBox VM Manager.")
            sys.exit(0)
        else:
            print("Invalid selection, please try again.")


if __name__ == "__main__":
    # Create a blank log file if it doesn't exist, just to ensure logging is set up
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w') as f:
            f.write("VM Manager Log\n")

    logging.info("VM Manager script started.")
    main_menu()
    logging.info("VM Manager script exited.")
