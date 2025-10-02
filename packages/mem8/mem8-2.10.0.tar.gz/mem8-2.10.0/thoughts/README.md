# Shared Thoughts Repository

Shared thoughts repository for AI-assisted development and knowledge management.

## Structure

```
thoughts/
├── shared/                    # Team-wide documents
│   ├── plans/                # Implementation plans
│   ├── research/             # Research documents  
│   ├── tickets/              # Linear tickets (ENG-XXXX.md)
│   ├── prs/                  # PR descriptions
│   └── decisions/            # Technical decisions
├── vaski/                  # Personal thoughts
│   ├── tickets/              # Personal ticket copies
│   ├── notes/               # Personal notes
│   └── archive/             # Archived thoughts
├── global/                   # Cross-repository thoughts
│   └── shared/              # Global shared patterns
└── searchable/              # Unified search directory
    ├── shared/ -> ../shared/
    ├── vaski/ -> ../vaski/
    └── global/ -> ../global/
```

## Usage

### Creating Documents

**Research Documents:**
```bash
# Timestamped research files
thoughts/shared/research/YYYY-MM-DD_HH-MM-SS_topic.md
```

**Implementation Plans:**
```bash
# Descriptive plan names
thoughts/shared/plans/fix-authentication-flow.md
```

**Ticket References:**
```bash
# Linear ticket format
thoughts/shared/tickets/ENG-1234.md
```

### Syncing Changes


Use the provided sync scripts:
```bash
# Windows
./sync-thoughts.bat

# Unix/Linux
./sync-thoughts.sh
```


Or manually with git:
```bash
git add thoughts/
git commit -m "Update thoughts: brief description"
git push origin main
```

## Integration

This thoughts directory integrates with:
- Claude Code `.claude` configurations
- Linear ticket management
- GitHub PR workflows
- Cross-project knowledge sharing

## File Naming Conventions

- **Research**: `YYYY-MM-DD_HH-MM-SS_topic.md`
- **Plans**: `descriptive-name.md`
- **Tickets**: `ENG-XXXX.md` (Linear format)
- **PRs**: `{number}_description.md`
- **Notes**: Free-form naming

## Repository Integration

- **GitHub URL**: https://github.com/your-org/thoughts
- **Project Root**: C:/Users/vaski/projects
- **Username**: vaski

## Searchable Directory

The `searchable/` directory contains links to all content for unified searching:
- Use grep, ripgrep, or IDE search across `searchable/`
- Always reference actual paths in documentation: `thoughts/shared/...`
- Links are maintained automatically