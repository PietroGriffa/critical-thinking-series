# Contributing to Critical Thinking Series

Thank you for your interest in contributing to the Critical Thinking Series! This guide will help you get started.

## How to Contribute

### Adding New Topics

1. **Create a new topic folder** following the naming convention: `topics/NN-topic-slug/`
2. **Add required files**:
   - `topic.yaml` - Machine-readable metadata
   - `README.md` - Topic overview
   - `slides.pdf` - Presentation slides (when available)
   - `handout.pdf` - Take-home materials (when available)
   - `demo/` - Interactive demonstrations
   - `references.md` - Additional resources

### Topic Metadata Format

Each `topic.yaml` must include:

```yaml
title: "Topic Title"
slug: "topic-slug"
number: N
date: "YYYY-MM-DD"
duration: 60  # minutes
presenter: "Presenter Name"
description: "Brief description of the topic"
objectives:
  - "Learning objective 1"
  - "Learning objective 2"
tags:
  - "tag1"
  - "tag2"
status: "planned|in-progress|completed"
materials:
  slides: "slides.pdf"
  handout: "handout.pdf"
  demo: "demo/"
  references: "references.md"
```

### Updating Documentation

1. Add corresponding documentation in `docs/topics/NN-topic-slug.md`
2. Update `mkdocs.yml` navigation if needed
3. The catalog in `README.md` will auto-update via GitHub Actions

### Submitting Changes

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-topic`
3. Make your changes following the structure above
4. Test that your changes work:
   - Run `python scripts/update_catalog.py` to update the catalog
   - Run `mkdocs serve` to test documentation locally
5. Submit a pull request with a clear description

## Quality Guidelines

- **Accuracy**: Ensure all content is factually correct
- **Accessibility**: Use clear, jargon-free language when possible
- **Practical**: Include real-world examples and exercises
- **Interactive**: Provide hands-on activities for engagement
- **References**: Include credible sources for further learning

## File Naming Conventions

- **Topic folders**: `NN-topic-slug/` (zero-padded numbers)
- **Files**: Use lowercase with hyphens for spaces
- **Demo files**: Descriptive names in `demo/` folder

## Review Process

All contributions will be reviewed for:

- Content accuracy and quality
- Consistency with series format
- Proper file structure and naming
- Working links and references
- Clear learning objectives

## Questions?

Open an issue in the repository if you have questions about contributing or need clarification on any guidelines.