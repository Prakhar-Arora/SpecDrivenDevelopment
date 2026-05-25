"""
Science Quiz Questions - Challenging and Advanced
"""

from app.models import QuizData

SCIENCE_QUIZZES = [
    QuizData(
        hints=[
            "I am a fundamental force related to mass-energy equivalence.",
            "I describe how massive objects curve spacetime itself.",
            "I replaced Newton's theory with a geometric interpretation.",
            "Einstein published my field equations in 1915.",
        ],
        answer="General Relativity",
    ),
    QuizData(
        hints=[
            "I am the maximum possible entropy change when heat is transferred.",
            "I measure disorder and irreversibility in thermodynamic systems.",
            "Boltzmann quantified me through statistical mechanics.",
            "I am central to the Second Law of Thermodynamics.",
        ],
        answer="Entropy",
    ),
    QuizData(
        hints=[
            "I am the study of matter composed of quarks and leptons.",
            "The Standard Model attempts to explain my three fundamental forces.",
            "I operate at subatomic scales and exhibit wave-particle duality.",
            "I unified electricity, magnetism, and weak nuclear forces.",
        ],
        answer="Quantum Field Theory",
    ),
    QuizData(
        hints=[
            "I am a self-replicating molecule that uses catalytic proteins.",
            "The Miller-Urey experiment created organic molecules under my conditions.",
            "I am the hypothetical chemical precursor to life.",
            "I required primordial soup and energy from lightning or UV radiation.",
        ],
        answer="Abiogenesis",
    ),
    QuizData(
        hints=[
            "I am a star that has collapsed into a singular point.",
            "My event horizon defines where escape velocity exceeds light speed.",
            "Hawking radiation can cause me to evaporate over cosmic timescales.",
            "I am formed when massive stars collapse at the end of their lives.",
        ],
        answer="Black Hole",
    ),
    QuizData(
        hints=[
            "I am the tendency of materials to return to original shape after deformation.",
            "My modulus describes stiffness for tensile stress.",
            "Hooke's Law quantifies me as stress proportional to strain.",
            "I fail when stress exceeds my yield point.",
        ],
        answer="Elasticity",
    ),
    QuizData(
        hints=[
            "I am the study of the origin and evolution of the universe.",
            "The Cosmic Microwave Background is key evidence for my Big Bang model.",
            "I explain the redshift of distant galaxies using Hubble's Law.",
            "Dark matter and dark energy dominate my composition.",
        ],
        answer="Cosmology",
    ),
    QuizData(
        hints=[
            "I am the branch of chemistry studying reaction rates and mechanisms.",
            "Activation energy determines whether I proceed rapidly or slowly.",
            "Transition state theory explains my rate-limiting steps.",
            "Catalysts speed me up without being consumed.",
        ],
        answer="Chemical Kinetics",
    ),
    QuizData(
        hints=[
            "I am a principle stating that the total energy in an isolated system remains constant.",
            "I cannot be created or destroyed, only transformed.",
            "I explain energy conversions between kinetic, potential, and other forms.",
            "I am fundamental to thermodynamics and mechanics.",
        ],
        answer="Conservation of Energy",
    ),
    QuizData(
        hints=[
            "I am the study of substances without carbon-hydrogen bonds.",
            "I include minerals, salts, and coordination complexes.",
            "I contrast with organic chemistry's carbon-based focus.",
            "Transition metals are central to my field.",
        ],
        answer="Inorganic Chemistry",
    ),
    QuizData(
        hints=[
            "I am a theoretical framework uniting quantum mechanics and general relativity.",
            "I propose that spacetime itself is quantized into Planck-scale loops.",
            "String theory and me compete to explain quantum gravity.",
            "Ashtekar formulated my mathematical foundations.",
        ],
        answer="Loop Quantum Gravity",
    ),
    QuizData(
        hints=[
            "I am the hypothesis that the universe is fine-tuned for observer existence.",
            "Weak anthropic principle and strong versions of me exist.",
            "I explain why physical constants appear precisely calibrated for life.",
            "Multiverse theory often accompanies discussion of me.",
        ],
        answer="Anthropic Principle",
    ),
    QuizData(
        hints=[
            "I am the phenomenon where light bends around massive objects.",
            "I was first observed during the 1919 solar eclipse expedition.",
            "I provides evidence for General Relativity's predictions.",
            "I create Einstein rings and gravitational lensing effects.",
        ],
        answer="Gravitational Lensing",
    ),
    QuizData(
        hints=[
            "I am a state of matter with separated ions and free electrons.",
            "I constitute 99% of the observable matter in the universe.",
            "Stars and nebulae are predominantly composed of me.",
            "I conduct electricity and respond to magnetic fields.",
        ],
        answer="Plasma",
    ),
]
