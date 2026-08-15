# Master Copywriting Skill - Makefile
# Cross-platform build automation

PYTHON ?= python3
SKILL_ROOT ?= .

.PHONY: all validate test standard agentic package clean version

all: package

validate:
	$(PYTHON) scripts/validate_skill.py $(SKILL_ROOT)

test:
	$(PYTHON) scripts/run_regression.py --all

standard:
	$(PYTHON) scripts/build_package.py --standard

agentic:
	$(PYTHON) scripts/build_package.py --agentic

package: validate
	$(PYTHON) scripts/run_regression.py --all
	$(PYTHON) scripts/build_package.py --all --clean

clean:
	rm -rf build dist

version:
	@echo "Master Copywriting Skill"
	@grep "^version:" SKILL.md | head -1

help:
	@echo "Master Copywriting Skill - Build Commands"
	@echo ""
	@echo "  make validate    Run skill structure validation"
	@echo "  make test        Run all regression test suites"
	@echo "  make standard    Build standard distribution package"
	@echo "  make agentic     Build agentic distribution package"
	@echo "  make package     Validate → Test → Build all (clean)"
	@echo "  make clean       Remove build/ and dist/ directories"
	@echo "  make version     Show skill version"
