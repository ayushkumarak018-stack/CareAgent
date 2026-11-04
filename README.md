# CareAgent: AI Healthcare & Medication Companion

**CareAgent** is an intelligent, compassionate AI agent built with the **Strands Agents SDK** for the *Strands SDK: Workshop to Ship* hackathon. It addresses critical healthcare challenges in underserved populations by bridging health literacy gaps, ensuring medication safety, and providing rapid emergency triage.

## 🌟 Focus Area & Social Impact
- **Focus Area**: Health & Accessibility
- **Target Population**: Underserved communities, elderly patients, and individuals with limited health literacy or limited access to primary care physicians.
- **Problem Addressed**: Medication non-adherence due to confusing medical jargon, dangerous accidental drug-drug interactions, and delayed emergency symptom triage.

---

## 🛠️ Key Features
1. **Plain-Language Prescription Explainer**: Translates complex prescription labels and medical jargon into clear, actionable, multilingual guidance.
2. **Drug-Drug Interaction Checker**: Screens multi-medication lists for critical adverse interactions and warns patients before harm occurs.
3. **Emergency Symptom Triage**: Rapidly screens user-reported symptoms for emergency red flags and instantly escalates to emergency services when high risk is detected.

---

## 🚀 Architecture & Strands SDK Integration
Built using the **Strands Agents SDK** (`strands.Agent` and `@tool`), CareAgent leverages:
- **Custom Agent Harness**: Structured system prompts and tool bindings.
- **Vended & Custom Tools**: Modular Python functions decorated with `@tool` for medical translation, safety verification, and triage.
- **Flexible Model Provider Support**: Works seamlessly with OpenAI, Amazon Bedrock, Anthropic, or Ollama.

---

## 📦 Quickstart
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your model API key (e.g. `OPENAI_API_KEY`):
   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```
3. Run the agent:
   ```bash
   python agent.py
   ```
