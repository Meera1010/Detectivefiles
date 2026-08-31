import json
import random

def generate_cases():
    cases = []
    names = ["The Whispering Shadows", "Echoes of the Past", "Midnight at the Manor", "The Crimson Enigma",
             "Silence of the Sea", "The Clockwork Alibi", "Phantom of the Opera House", "The Last Train to Nowhere",
             "A Study in Scarlet", "The Jade Dagger"]
    
    for i, title in enumerate(names):
        case = {
            "title": title,
            "description": f"A complex investigation into the events of {title}.",
            "difficulty": random.choice(["Easy", "Medium", "Hard", "Expert"]),
            "evidence": [],
            "suspects": [],
            "clues": [],
            "timeline": []
        }
        
        # Generate 50 evidence items per case
        for j in range(50):
            case["evidence"].append({
                "name": f"Evidence {j+1}",
                "type": random.choice(["document", "physical", "photo", "digital"]),
                "description": f"Detailed description for evidence {j+1}." * 20
            })
            
        # Generate 15 suspects per case
        for j in range(15):
            suspect = {
                "name": f"Suspect {j+1}",
                "profile": f"Profile description for suspect {j+1}." * 20,
                "interviews": []
            }
            # Generate 20 interview nodes per suspect
            for k in range(20):
                suspect["interviews"].append({
                    "question": f"Question {k+1} for {suspect['name']}",
                    "answer": f"Answer {k+1} from {suspect['name']}." * 10
                })
            case["suspects"].append(suspect)
            
        # Generate 100 timeline events
        for j in range(100):
            case["timeline"].append({
                "time": f"{10 + (j%14)}:00",
                "event": f"Timeline event {j+1} description." * 10
            })
            
        cases.append(case)
        
    with open('cases_data.json', 'w') as f:
        json.dump(cases, f, indent=4)
    print("Generated cases_data.json")

if __name__ == "__main__":
    generate_cases()
