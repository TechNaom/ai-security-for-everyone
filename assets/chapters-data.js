/*
  Single source of truth for the AI Security for Everyone chapter
  roster. Mirrors the ai-coding-agents-for-everyone pattern: sidebar.js
  and home.js render navigation from this file. A chapter is "live" iff
  it has a `path` -- omit `path` for chapters that don't exist yet, do
  not set a placeholder path, or sidebar/home will link to a 404. The
  same rule applies to a module's `examPath`: set it to null until that
  module's written exam actually exists in assessments/written-exams/.
  No chapters have content yet -- see PROJECT_STATE.md.
*/

window.AISFE_MODULES = [
  {
    title: "Module 1 — Threat Modeling LLM Systems",
    summary: "A structured way to think about LLM attack surface before diving into any specific attack.",
    examPath: null,
    chapters: [
      {
        id: "chapter-01",
        num: 1,
        title: "Threat Modeling LLM Systems: The OWASP Top 10 for LLM Applications",
        description: "A working checklist for LLM attack surface, not trivia to memorize.",
        path: "chapters/chapter-01-threat-modeling-llm-systems-owasp-top-10/lesson.html"
      },
      {
        id: "chapter-02",
        num: 2,
        title: "Mapping the Attack Surface of a Real LLM Feature",
        description: "Applying the threat model to a real, given feature end to end.",
        path: "chapters/chapter-02-mapping-the-attack-surface-of-a-real-llm-feature/lesson.html"
      }
    ]
  },
  {
    title: "Module 2 — Prompt Injection Deep Dive",
    summary: "The single most consequential LLM-specific vulnerability class, covered in real depth.",
    examPath: "assessments/written-exams/module-2-exam.html",
    chapters: [
      {
        id: "chapter-03",
        num: 3,
        title: "Direct Prompt Injection",
        description: "How it works, mechanically, and why it's not a solved problem.",
        path: "chapters/chapter-03-direct-prompt-injection/lesson.html"
      },
      {
        id: "chapter-04",
        num: 4,
        title: "Indirect Prompt Injection and Jailbreaking Techniques",
        description: "Attacks carried through untrusted content, and real jailbreak patterns.",
        path: "chapters/chapter-04-indirect-prompt-injection-and-jailbreaking-techniques/lesson.html"
      },
      {
        id: "chapter-05",
        num: 5,
        title: "Evaluating Prompt-Injection Defenses Honestly",
        description: "What a defense actually stops versus what it claims to stop.",
        path: "chapters/chapter-05-evaluating-prompt-injection-defenses-honestly/lesson.html"
      }
    ]
  },
  {
    title: "Module 3 — Data & Model Integrity",
    summary: "Attacks on the model and its training/deployment pipeline, not just its runtime inputs.",
    examPath: null,
    chapters: [
      {
        id: "chapter-06",
        num: 6,
        title: "Data Poisoning",
        description: "How training and fine-tuning data becomes an attack vector.",
        path: "chapters/chapter-06-data-poisoning/lesson.html"
      },
      {
        id: "chapter-07",
        num: 7,
        title: "Model Extraction and Theft",
        description: "How a model's behavior or weights can be stolen through its API.",
        path: "chapters/chapter-07-model-extraction-and-theft/lesson.html"
      },
      {
        id: "chapter-08",
        num: 8,
        title: "Supply-Chain Risk: Weights, Dependencies, and Provenance",
        description: "Trusting what you didn't train yourself.",
        path: "chapters/chapter-08-supply-chain-risk-weights-dependencies-and-provenance/lesson.html"
      }
    ]
  },
  {
    title: "Module 4 — Securing RAG & Agentic Systems",
    summary: "Applying this course's depth to the two system shapes most real LLM products actually take.",
    examPath: null,
    chapters: [
      {
        id: "chapter-09",
        num: 9,
        title: "Securing RAG Pipelines Against Injection",
        description: "Injection risk carried through retrieved documents.",
        path: "chapters/chapter-09-securing-rag-pipelines-against-injection/lesson.html"
      },
      {
        id: "chapter-10",
        num: 10,
        title: "Securing Agentic Systems Against Adversarial Tool Output",
        description: "Extending an agent's permission model against a malicious tool result."
      }
    ]
  },
  {
    title: "Module 5 — Red-Teaming & Output Handling",
    summary: "The practitioner half: running a real red-team exercise and handling output safely.",
    examPath: null,
    chapters: [
      {
        id: "chapter-11",
        num: 11,
        title: "Red-Teaming an LLM System: Methodology and Practice",
        description: "A structured red-team exercise against a real target, with a findings report."
      },
      {
        id: "chapter-12",
        num: 12,
        title: "Handling LLM Output Safely: PII and Downstream Injection Risk",
        description: "What a model outputs can itself be an attack vector."
      }
    ]
  },
  {
    title: "Module 6 — Capstone",
    summary: "Architect-level synthesis.",
    examPath: null,
    chapters: [
      {
        id: "chapter-13",
        num: 13,
        title: "Capstone: Security Architecture for a Real LLM System",
        description: "A Level 4 architecture challenge closing the course."
      }
    ]
  }
];
