<<<<<<< HEAD

# Online Polling and Voting System

candidates = ["Candidate A", "Candidate B", "Candidate C"]
votes = [0, 0, 0]
voted_users = set()

while True:
    print("\n--- ONLINE POLLING SYSTEM ---")
    print("1. Vote")
    print("2. Display Results")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        voter_id = input("Enter Voter ID: ").strip().lower()

        if not voter_id:
            print("Voter ID cannot be empty!")
            continue

        if voter_id in voted_users:
            print("You have already voted!")
            continue

        print("\nCandidates:")
        for i, candidate in enumerate(candidates, start=1):
            print(f"{i}. {candidate}")

        try:
            vote = int(input("Enter your vote: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if 1 <= vote <= len(candidates):
            votes[vote - 1] += 1
            voted_users.add(voter_id)
            print("Vote recorded successfully!")
            print("\n--- Live Results ---")
            total_votes = sum(votes)
            for i, candidate in enumerate(candidates):
                percentage = votes[i] / total_votes * 100
                print(f"{candidate}: {votes[i]} votes ({percentage:.2f}%)")
            print("Total Votes:", total_votes)
        else:
            print("Invalid candidate!")

    elif choice == "2":
        print("\n--- POLLING RESULTS ---")
        total_votes = sum(votes)

        for i, candidate in enumerate(candidates):
            percentage = (
                votes[i] / total_votes * 100
                if total_votes > 0 else 0
            )
            print(
                f"{candidate}: {votes[i]} votes "
                f"({percentage:.2f}%)"
            )

        print("Total Votes:", total_votes)

    elif choice == "3":
        print("Thank you for voting!")
        break

    else:
        print("Invalid choice! Please enter 1, 2 or 3.")
=======

# Online Polling and Voting System

candidates = ["Candidate A", "Candidate B", "Candidate C"]
votes = [0, 0, 0]
voted_users = set()

while True:
    print("\n--- ONLINE POLLING SYSTEM ---")
    print("1. Vote")
    print("2. Display Results")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        voter_id = input("Enter Voter ID: ").strip()

        if not voter_id:
            print("Voter ID cannot be empty!")
            continue

        if voter_id in voted_users:
            print("You have already voted!")
            continue

        print("\nCandidates:")
        for i, candidate in enumerate(candidates, start=1):
            print(f"{i}. {candidate}")

        try:
            vote = int(input("Enter your vote: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if 1 <= vote <= len(candidates):
            votes[vote - 1] += 1
            voted_users.add(voter_id)
            print("Vote recorded successfully!")
        else:
            print("Invalid candidate!")

    elif choice == "2":
        print("\n--- POLLING RESULTS ---")
        total_votes = sum(votes)

        for i, candidate in enumerate(candidates):
            percentage = (
                votes[i] / total_votes * 100
                if total_votes > 0 else 0
            )
            print(
                f"{candidate}: {votes[i]} votes "
                f"({percentage:.2f}%)"
            )

        print("Total Votes:", total_votes)

    elif choice == "3":
        print("Thank you for voting!")
        break

    else:
        print("Invalid choice! Please enter 1, 2 or 3.")
>>>>>>> 5d3e79be50aa7ba5826f870312cc467adef59b94
