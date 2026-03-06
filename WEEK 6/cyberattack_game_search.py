import math

attacker = {"Exploit": -3, "Phishing": -2, "Malware": -4}
defender = {"Patch": +3, "Monitor": +2, "Restore": +4}

score = 5
for turn in range(3):
    print(f"System security: {score}")
    print("Available defenses:", list(defender.keys()))
    act = input("Choose your defense: ")
    if act not in defender:
        print("Invalid! Using default: Patch")
        act = "Patch"
    print(f"Defender chooses: {act}, effect: {defender[act]}")
    
    # Attacker chooses worst move
    att = min(attacker, key=attacker.get)
    print(f"Attacker chooses: {att}, effect: {attacker[att]}")
    
    # Update system score
    score += defender[act] + attacker[att]
    print(f"New system security: {score}\n")