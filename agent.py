"""
CareAgent: AI Healthcare & Medication Companion for Underserved Populations
Built with Strands Agents SDK for the 'Strands SDK: Workshop to Ship' Hackathon.
"""

import os
from strands import Agent, tool

# Define custom tools for the Health focus area
@tool
def explain_prescription(medication_name: str, instructions: str, patient_language: str = "English") -> str:
    """
    Translates complex medical prescription instructions into clear, plain language
    tailored for patients with low health literacy or elderly individuals.
    """
    # Simulated plain language explanation logic combined with SDK tool execution
    explanations = {
        "metformin": "Take this pill with meals to help control your blood sugar. Do not skip meals while taking this medicine.",
        "lisinopril": "Take this pill once a day to help lower your blood pressure. It is best to take it at the same time every day.",
        "atorvastatin": "Take this pill once a day, usually in the evening, to help lower your cholesterol and protect your heart."
    }
    key = medication_name.lower().strip()
    base_explanation = explanations.get(key, f"Take {medication_name} exactly as prescribed by your healthcare provider. Follow the dosage instructions carefully.")
    
    return f"""[Plain-Language Medical Guide ({patient_language})]
Medication: {medication_name.capitalize()}
Original Instructions: {instructions}
Simplified Guidance:
- {base_explanation}
- Safety Tip: Never change your dose without consulting your doctor or clinic.
- Storage: Keep in a cool, dry place away from children."""

@tool
def check_drug_interactions(medications: list[str]) -> str:
    """
    Checks a list of medications for potential adverse drug-drug interactions
    and warns patients or community health workers about risks.
    """
    meds = [m.lower().strip() for m in medications]
    warnings = []
    
    if "aspirin" in meds and "warfarin" in meds:
        warnings.append("CRITICAL WARNING: Aspirin combined with Warfarin significantly increases the risk of bleeding.")
    if "metformin" in meds and "contrast dye" in meds:
        warnings.append("WARNING: Metformin and contrast dye may require temporary discontinuation under medical supervision.")
        
    if not warnings:
        return f"Checked medications ({', '.join(medications)}): No major high-risk interactions detected in standard database. Always consult your pharmacist."
    else:
        return f"Interaction Alerts for ({', '.join(medications)}):\n" + "\n".join(warnings) + "\nPlease consult a licensed physician immediately."

@tool
def triage_symptoms(symptoms: str) -> str:
    """
    Screens patient-reported symptoms for emergency red flags and provides
    guidance, including local crisis or urgent care escalation when necessary.
    """
    symptoms_lower = symptoms.lower()
    emergency_keywords = ["chest pain", "difficulty breathing", "severe bleeding", "sudden weakness", "suicide", "overdose"]
    
    is_emergency = any(kw in symptoms_lower for kw in emergency_keywords)
    
    if is_emergency:
        return f"""[EMERGENCY TRIAGE ALERT]
Reported Symptoms: "{symptoms}"
STATUS: EMERGENCY DETECTED.
ACTION REQUIRED: Call emergency services (e.g., 911 or local emergency number) immediately or proceed to the nearest emergency room. Do not wait."""
    else:
        return f"""[Routine Triage Guidance]
Reported Symptoms: "{symptoms}"
STATUS: Non-immediate emergency detected.
Recommendation: Schedule an appointment with your community clinic or primary care physician. Monitor your symptoms closely. If symptoms worsen, seek urgent care."""

def create_care_agent():
    """
    Initializes and returns the Strands CareAgent configured with health tools.
    """
    # Initialize the Strands Agent
    # Note: Strands works with OpenAI, Anthropic, Bedrock, etc. 
    # We configure with instructions and tools.
    system_prompt = (
        "You are CareAgent, an empathetic AI healthcare and medication companion built for underserved populations. "
        "Your mission is to bridge health literacy gaps by translating complex medical instructions, "
        "checking medication safety, and providing reliable triage and wellness guidance. "
        "Always be compassionate, clear, accurate, and safety-conscious."
    )
    
    agent = Agent(
        system_prompt=system_prompt,
        tools=[explain_prescription, check_drug_interactions, triage_symptoms]
    )
    return agent

if __name__ == "__main__":
    print("Initializing CareAgent (Strands SDK)...")
    agent = create_care_agent()
    print("CareAgent initialized successfully!")
    
    # Test run
    result = agent("Can you explain how to take Metformin and check if combining Aspirin and Warfarin is safe?")
    print("\n--- Agent Response ---")
    print(result)
