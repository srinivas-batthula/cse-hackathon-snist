# data/skills.py

SKILL_ORDER = [
    # ─── Version Control ───
    "git",
    "github",
    "github flow",

    # ─── Programming Languages ───
    "c",
    "c++",
    "java",
    "python",
    "javascript",
    "typescript",

    # ─── Frontend Basics ───
    "html",
    "css",
    "responsive design",
    "dom manipulation",

    # ─── Frontend Styling Libraries ───
    "bootstrap",
    "tailwindcss",
    "material ui",
    "chakra ui",

    # ─── Frontend Frameworks/Libraries ───
    "react",
    "next.js",
    "vue",
    "angular",
    "svelte",

    # ─── State Management ───
    "redux",
    "context api",
    "zustand",

    # ─── Backend Basics ───
    "node.js",
    "express.js",
    "flask",
    "django",
    "rest apis",

    # ─── Databases ───
    "mongodb",
    "postgresql",
    "mysql",
    "sqlite",

    # ─── Authentication ───
    "jwt",
    "oauth",

    # ─── DevOps & CI/CD ───
    "docker",
    "docker compose",
    "kubernetes",
    "ci/cd",
    "github actions",
    "jenkins",

    # ─── Advanced Backend & Scaling ───
    "redis",
    "websockets",
    "graphql",
    "grpc",
    "message queues",
    "rabbitmq",
    "kafka",

    # ─── Testing ───
    "unit testing",
    "jest",
    "mocha",
    "chai",
    "cypress",
    "testing",

    # ─── Cloud Platforms ───
    "aws",
    "azure",
    "gcp",
    "firebase",
    "netlify",
    "vercel",

    # ─── Deployment ───
    "deployment",
    "nginx",
    "load balancing",
    "monitoring",
    "logging"
]


## _-_-_-_-_-_-_-_-_-_ -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ -_-_-_-_-_-_-_-_- ##


LEARNING_PATH_DB = {
    "React": {
        "modules": ["JSX Basics", "Components & Props", "State & Lifecycle", "Hooks", "Context API", "React Project"],
        "refs": ["https://reactjs.org/docs/getting-started.html", "https://www.geeksforgeeks.org/reactjs/"]
    },
    "Node.js": {
        "modules": ["Intro to Node", "Express.js", "REST APIs", "Middleware", "JWT Auth"],
        "refs": ["https://nodejs.org/en/docs", "https://www.geeksforgeeks.org/node-js/"]
    },
    "MongoDB": {
        "modules": ["Data Modeling", "CRUD Ops", "Mongoose", "Aggregation", "Indexes"],
        "refs": ["https://www.mongodb.com/docs/", "https://www.geeksforgeeks.org/mongodb/"]
    },
    "Python": {
        "modules": ["Syntax", "Data Structures", "OOP", "Flask API", "Projects"],
        "refs": ["https://docs.python.org/3/", "https://www.geeksforgeeks.org/python/"]
    },
    "Docker": {
        "modules": ["Images & Containers", "Volumes", "Dockerfile", "Compose", "Deploy"],
        "refs": ["https://docs.docker.com/get-started/", "https://www.geeksforgeeks.org/docker/"]
    },
    "Git": {
        "modules": ["init, add, commit", "Branching", "Merging", "Pull Request", "GitHub Flow"],
        "refs": ["https://git-scm.com/docs", "https://www.atlassian.com/git/tutorials"]
    },
    "HTML": {
        "modules": ["HTML Basics", "Forms & Inputs", "Semantic Tags", "Media Embedding", "SEO Best Practices"],
        "refs": ["https://developer.mozilla.org/en-US/docs/Web/HTML", "https://www.w3schools.com/html/"]
    },
    "CSS": {
        "modules": ["Selectors", "Box Model", "Flexbox", "Grid", "Responsive Design"],
        "refs": ["https://developer.mozilla.org/en-US/docs/Web/CSS", "https://css-tricks.com/"]
    },
    "JavaScript": {
        "modules": ["Variables & Types", "Functions", "DOM Manipulation", "Async JS", "ES6+"],
        "refs": ["https://developer.mozilla.org/en-US/docs/Web/JavaScript", "https://javascript.info/"]
    },
    "TypeScript": {
        "modules": ["Types", "Interfaces", "Generics", "Decorators", "TS + React"],
        "refs": ["https://www.typescriptlang.org/docs/", "https://www.geeksforgeeks.org/typescript/"]
    },
    "Express.js": {
        "modules": ["Routing", "Middleware", "Error Handling", "REST APIs", "Security"],
        "refs": ["https://expressjs.com/en/starter/installing.html", "https://www.geeksforgeeks.org/express-js/"]
    },
    "Flask": {
        "modules": ["Routing", "Jinja2 Templating", "APIs", "Flask-SQLAlchemy", "Deployment"],
        "refs": ["https://flask.palletsprojects.com/en/latest/", "https://www.geeksforgeeks.org/python-flask/"]
    },
    "FastAPI": {
        "modules": ["Path Params", "Query Params", "Pydantic Models", "Dependency Injection", "Rate Limiting"],
        "refs": ["https://fastapi.tiangolo.com/", "https://www.geeksforgeeks.org/python-fastapi/"]
    },
    "SQL": {
        "modules": ["DDL & DML", "Joins", "Indexes", "Subqueries", "Stored Procedures"],
        "refs": ["https://www.w3schools.com/sql/", "https://sqlzoo.net/"]
    },
    "PostgreSQL": {
        "modules": ["Data Types", "Constraints", "Functions", "Indexes", "Performance Tuning"],
        "refs": ["https://www.postgresql.org/docs/", "https://www.geeksforgeeks.org/postgresql/"]
    },
    "MySQL": {
        "modules": ["Database Design", "Queries", "Stored Procedures", "Triggers", "User Management"],
        "refs": ["https://dev.mysql.com/doc/", "https://www.geeksforgeeks.org/mysql/"]
    },
    "Linux": {
        "modules": ["Shell Basics", "File Permissions", "Process Management", "Networking", "Bash Scripting"],
        "refs": ["https://linuxjourney.com/", "https://www.geeksforgeeks.org/linux-commands/"]
    },
    "AWS": {
        "modules": ["EC2", "S3", "Lambda", "IAM", "Deployments"],
        "refs": ["https://docs.aws.amazon.com/", "https://www.geeksforgeeks.org/amazon-web-services/"]
    },
    "Firebase": {
        "modules": ["Firestore", "Auth", "Hosting", "Cloud Functions", "Realtime DB"],
        "refs": ["https://firebase.google.com/docs", "https://www.geeksforgeeks.org/firebase/"]
    },
    "Kubernetes": {
        "modules": ["Pods", "Services", "Deployments", "Volumes", "Helm"],
        "refs": ["https://kubernetes.io/docs/home/", "https://www.geeksforgeeks.org/kubernetes/"]
    },
    "Jenkins": {
        "modules": ["Pipelines", "Declarative Syntax", "Build Triggers", "Docker + Jenkins", "CI/CD"],
        "refs": ["https://www.jenkins.io/doc/", "https://www.geeksforgeeks.org/jenkins/"]
    },
    "GraphQL": {
        "modules": ["Schemas", "Queries & Mutations", "Resolvers", "Apollo Server", "Auth"],
        "refs": ["https://graphql.org/learn/", "https://www.apollographql.com/docs/"]
    },
    "WebSockets": {
        "modules": ["Basics", "Socket.IO", "Realtime Chat", "Rooms", "Scalability"],
        "refs": ["https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API", "https://socket.io/docs/v4/"]
    },
    "REST API Design": {
        "modules": ["HTTP Methods", "Status Codes", "Versioning", "Pagination", "Auth"],
        "refs": ["https://restfulapi.net/", "https://developer.mozilla.org/en-US/docs/Web/HTTP"]
    },
    "CI/CD": {
        "modules": ["Build", "Test", "Deploy", "GitHub Actions", "Docker Integration"],
        "refs": ["https://docs.github.com/en/actions", "https://www.geeksforgeeks.org/ci-cd-tools/"]
    },
    "OpenAI API": {
        "modules": ["API Setup", "Chat Completion", "Rate Limits", "Prompt Engineering", "Use Cases"],
        "refs": ["https://platform.openai.com/docs", "https://www.geeksforgeeks.org/openai-api/"]
    },
    "Next.js": {
        "modules": ["Pages & Routing", "API Routes", "SSR vs SSG", "Deployment", "Auth"],
        "refs": ["https://nextjs.org/docs", "https://www.geeksforgeeks.org/next-js/"]
    },
    "Tailwind CSS": {
        "modules": ["Utility Classes", "Responsive Design", "Dark Mode", "Plugins", "Custom Themes"],
        "refs": ["https://tailwindcss.com/docs", "https://www.geeksforgeeks.org/tailwind-css/"]
    },
    "Redux": {
        "modules": ["Store", "Reducers", "Actions", "Middleware", "Redux Toolkit"],
        "refs": ["https://redux.js.org/", "https://www.geeksforgeeks.org/redux/"]
    },
    "OAuth2": {
        "modules": ["Flow Overview", "Access Tokens", "Scopes", "PKCE", "JWT Integration"],
        "refs": ["https://oauth.net/2/", "https://auth0.com/docs"]
    }
}
