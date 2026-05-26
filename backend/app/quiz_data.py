"""Quiz question pools for all categories.

Contains 8 questions per category (Science, History, Celebrity),
each with 5 progressive hints ordered from general to specific.
"""

QUIZ_POOLS = {
    "science": [
        {
            "id": "science_001",
            "category": "science",
            "hints": [
                {"order": 1, "text": "I am found throughout nature in various forms"},
                {"order": 2, "text": "I am essential to all living organisms"},
                {
                    "order": 3,
                    "text": "I can exist in three states: solid, liquid, and gas",
                },
                {"order": 4, "text": "I make up about 70% of the Earth's surface"},
                {"order": 5, "text": "My chemical formula is H2O"},
            ],
            "answer": "water",
        },
        {
            "id": "science_002",
            "category": "science",
            "hints": [
                {"order": 1, "text": "I am the most abundant element in the universe"},
                {"order": 2, "text": "I am the lightest element on the periodic table"},
                {
                    "order": 3,
                    "text": "Stars are mostly made of me and my isotope deuterium",
                },
                {"order": 4, "text": "I combine with oxygen to form water"},
                {"order": 5, "text": "My atomic number is 1"},
            ],
            "answer": "hydrogen",
        },
        {
            "id": "science_003",
            "category": "science",
            "hints": [
                {"order": 1, "text": "I am a fundamental force of nature"},
                {"order": 2, "text": "I keep planets orbiting stars"},
                {"order": 3, "text": "I cause objects to fall toward Earth"},
                {"order": 4, "text": "I am an inverse square law force"},
                {"order": 5, "text": "Isaac Newton described me mathematically"},
            ],
            "answer": "gravity",
        },
        {
            "id": "science_004",
            "category": "science",
            "hints": [
                {"order": 1, "text": "I am a form of energy"},
                {"order": 2, "text": "I travel in waves at a constant speed"},
                {"order": 3, "text": "I enable vision and photosynthesis"},
                {"order": 4, "text": "I consist of electromagnetic radiation"},
                {"order": 5, "text": "I travel at approximately 300,000 km/s"},
            ],
            "answer": "light",
        },
        {
            "id": "science_005",
            "category": "science",
            "hints": [
                {"order": 1, "text": "I am the powerhouse of the cell"},
                {"order": 2, "text": "I contain my own DNA"},
                {"order": 3, "text": "I generate ATP for cellular energy"},
                {"order": 4, "text": "I have a double membrane structure"},
                {"order": 5, "text": "I am found in eukaryotic cells"},
            ],
            "answer": "mitochondria",
        },
        {
            "id": "science_006",
            "category": "science",
            "hints": [
                {"order": 1, "text": "I am a gas at room temperature"},
                {"order": 2, "text": "Plants use me for photosynthesis"},
                {"order": 3, "text": "Humans exhale me after breathing"},
                {"order": 4, "text": "I am essential for combustion"},
                {"order": 5, "text": "My chemical formula is CO2"},
            ],
            "answer": "carbon dioxide",
        },
        {
            "id": "science_007",
            "category": "science",
            "hints": [
                {"order": 1, "text": "I am the basic unit of life"},
                {"order": 2, "text": "I contain a nucleus and organelles"},
                {"order": 3, "text": "I was discovered by Robert Hooke"},
                {"order": 4, "text": "All living things are made of me"},
                {"order": 5, "text": "I am a biological cell"},
            ],
            "answer": "cell",
        },
        {
            "id": "science_008",
            "category": "science",
            "hints": [
                {
                    "order": 1,
                    "text": "I am a phenomenon where waves bend around obstacles",
                },
                {"order": 2, "text": "I explain why you can hear around corners"},
                {"order": 3, "text": "I was studied extensively by Christiaan Huygens"},
                {"order": 4, "text": "I apply to all types of waves"},
                {"order": 5, "text": "My name comes from the Latin word for bending"},
            ],
            "answer": "diffraction",
        },
    ],
    "history": [
        {
            "id": "history_001",
            "category": "history",
            "hints": [
                {"order": 1, "text": "I occurred in North America in the late 1700s"},
                {"order": 2, "text": "I led to the creation of the United States"},
                {"order": 3, "text": "I was fought against British colonial rule"},
                {
                    "order": 4,
                    "text": "Declaration of Independence was signed during me",
                },
                {"order": 5, "text": "I began in 1775"},
            ],
            "answer": "American Revolution",
        },
        {
            "id": "history_002",
            "category": "history",
            "hints": [
                {"order": 1, "text": "I was a dark period in European history"},
                {"order": 2, "text": "I lasted approximately 1000 years"},
                {"order": 3, "text": "I followed the fall of the Roman Empire"},
                {"order": 4, "text": "I preceded the Renaissance"},
                {"order": 5, "text": "I am called the Middle Ages or Medieval period"},
            ],
            "answer": "Middle Ages",
        },
        {
            "id": "history_003",
            "category": "history",
            "hints": [
                {"order": 1, "text": "I was a global conflict lasting 6 years"},
                {"order": 2, "text": "I occurred from 1939-1945"},
                {"order": 3, "text": "I involved Nazi Germany and Imperial Japan"},
                {"order": 4, "text": "I was fought by the Allies against the Axis"},
                {"order": 5, "text": "I am World War Two"},
            ],
            "answer": "World War II",
        },
        {
            "id": "history_004",
            "category": "history",
            "hints": [
                {
                    "order": 1,
                    "text": "I was an Italian artist and polymath of the Renaissance",
                },
                {"order": 2, "text": "I painted the Mona Lisa"},
                {
                    "order": 3,
                    "text": "I designed flying machines centuries before aviation",
                },
                {"order": 4, "text": "I was born in Vinci, Italy"},
                {"order": 5, "text": "My name is Leonardo da Vinci"},
            ],
            "answer": "Leonardo da Vinci",
        },
        {
            "id": "history_005",
            "category": "history",
            "hints": [
                {"order": 1, "text": "I was an ancient Greek philosopher"},
                {"order": 2, "text": "I founded the Academy in Athens"},
                {"order": 3, "text": "I was a student of Socrates"},
                {"order": 4, "text": "I wrote The Republic"},
                {"order": 5, "text": "My name is Plato"},
            ],
            "answer": "Plato",
        },
        {
            "id": "history_006",
            "category": "history",
            "hints": [
                {"order": 1, "text": "I was a conflict between political ideologies"},
                {"order": 2, "text": "I lasted from 1947 to 1991"},
                {"order": 3, "text": "I was between Soviet Union and United States"},
                {"order": 4, "text": "I involved nuclear weapons threat"},
                {"order": 5, "text": "I am the Cold War"},
            ],
            "answer": "Cold War",
        },
        {
            "id": "history_007",
            "category": "history",
            "hints": [
                {"order": 1, "text": "I was a movement of rebirth and renewal"},
                {"order": 2, "text": "I occurred from 14th-17th centuries"},
                {"order": 3, "text": "I started in Italy and spread through Europe"},
                {
                    "order": 4,
                    "text": "I marked the transition from Middle Ages to modernity",
                },
                {"order": 5, "text": "I am the Renaissance"},
            ],
            "answer": "Renaissance",
        },
        {
            "id": "history_008",
            "category": "history",
            "hints": [
                {"order": 1, "text": "I was an Egyptian ruler"},
                {"order": 2, "text": "I united Upper and Lower Egypt"},
                {"order": 3, "text": "I built the Great Pyramid of Giza"},
                {"order": 4, "text": "I ruled during the Old Kingdom"},
                {"order": 5, "text": "My name is Pharaoh Khufu or Cheops"},
            ],
            "answer": "Khufu",
        },
    ],
    "celebrity": [
        {
            "id": "celebrity_001",
            "category": "celebrity",
            "hints": [
                {"order": 1, "text": "I am an American actor and filmmaker"},
                {"order": 2, "text": "I starred in the Rocky and Rambo franchises"},
                {
                    "order": 3,
                    "text": "I won an Academy Award for Best Picture as a producer",
                },
                {"order": 4, "text": "I am known for playing strong action heroes"},
                {"order": 5, "text": "My name is Sylvester Stallone"},
            ],
            "answer": "Sylvester Stallone",
        },
        {
            "id": "celebrity_002",
            "category": "celebrity",
            "hints": [
                {
                    "order": 1,
                    "text": "I am a British actor famous for portraying a secret agent",
                },
                {"order": 2, "text": "I am known for the James Bond film series"},
                {"order": 3, "text": "I have won multiple Academy Awards"},
                {"order": 4, "text": "I am associated with the role of 007"},
                {"order": 5, "text": "My most famous actor name is Sean Connery"},
            ],
            "answer": "Sean Connery",
        },
        {
            "id": "celebrity_003",
            "category": "celebrity",
            "hints": [
                {"order": 1, "text": "I am a South African entrepreneur and inventor"},
                {"order": 2, "text": "I founded Tesla and SpaceX"},
                {"order": 3, "text": "I aim to make humanity multi-planetary"},
                {"order": 4, "text": "I am known for innovative technology ventures"},
                {"order": 5, "text": "My name is Elon Musk"},
            ],
            "answer": "Elon Musk",
        },
        {
            "id": "celebrity_004",
            "category": "celebrity",
            "hints": [
                {"order": 1, "text": "I am an American singer and actress"},
                {"order": 2, "text": "I starred in high school musical films"},
                {"order": 3, "text": "I am known for my songs and acting career"},
                {"order": 4, "text": "I won a Grammy Award"},
                {"order": 5, "text": "My name is Zendaya"},
            ],
            "answer": "Zendaya",
        },
        {
            "id": "celebrity_005",
            "category": "celebrity",
            "hints": [
                {
                    "order": 1,
                    "text": "I am a British musician and former Beatles member",
                },
                {"order": 2, "text": "I am a legendary songwriter and performer"},
                {"order": 3, "text": "I won the Nobel Prize in Literature"},
                {"order": 4, "text": "I am associated with the 1960s counterculture"},
                {"order": 5, "text": "My name is Bob Dylan"},
            ],
            "answer": "Bob Dylan",
        },
        {
            "id": "celebrity_006",
            "category": "celebrity",
            "hints": [
                {
                    "order": 1,
                    "text": "I am an American talk show host and media personality",
                },
                {
                    "order": 2,
                    "text": "I host one of the most popular daytime talk shows",
                },
                {"order": 3, "text": "I am known for my philanthropic work"},
                {"order": 4, "text": "I have built a media empire"},
                {"order": 5, "text": "My name is Oprah Winfrey"},
            ],
            "answer": "Oprah Winfrey",
        },
        {
            "id": "celebrity_007",
            "category": "celebrity",
            "hints": [
                {"order": 1, "text": "I am a French mathematician and philosopher"},
                {
                    "order": 2,
                    "text": "I am known for the phrase 'I think, therefore I am'",
                },
                {"order": 3, "text": "I founded modern Western philosophy"},
                {"order": 4, "text": "I lived during the 17th century"},
                {"order": 5, "text": "My name is René Descartes"},
            ],
            "answer": "René Descartes",
        },
        {
            "id": "celebrity_008",
            "category": "celebrity",
            "hints": [
                {"order": 1, "text": "I am an American actor known for action films"},
                {"order": 2, "text": "I have appeared in major blockbuster franchises"},
                {"order": 3, "text": "I won an Academy Award for Best Actor"},
                {"order": 4, "text": "I am known for my charisma and diverse roles"},
                {"order": 5, "text": "My name is Will Smith"},
            ],
            "answer": "Will Smith",
        },
    ],
}
