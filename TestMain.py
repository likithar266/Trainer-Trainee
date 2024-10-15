import classes

# Main block to run the program
if __name__ == "__main__":
    # Take input for trainer name first
    trainer_name = input("Enter the trainer's name: ")

    # Take input for organization name
    org_name = input("Enter the organization name: ")
    org = classes.Organization(org_name)

    # Create trainer after organization has been input
    trainer = classes.Trainer(trainer_name, org)
    # Take input for number of trainees
    num_trainees = int(input("Enter the number of trainees: "))

    # Loop to take input for each trainee and add to the organization
    for i in range(num_trainees):
        trainee_name = input(f"Enter the name of trainee {i+1}: ")
        trainee = classes.Trainee(trainee_name, org)

    # Display results
    print("\n--- Organization Details ---")
    print("Organization Name:", org.getName())
    print("Trainer's Name:", trainer.name)
    print("Number of Trainees:", org.getNumOfTrainees())
