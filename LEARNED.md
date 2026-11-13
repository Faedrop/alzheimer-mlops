
# LEARNED

- Git: branch -> commit -> push -> PR -> merge -> pull. Never commit directly to main.
- .gitignore keeps data out of Git; DVC will version it instead.
- EDA: check class balance first, it decides the split and the metrics.
- Correlation sign matters: negative = higher value, lower diagnosis rate.
- Integer-coded categories (Gender, Ethnicity, EducationLevel) must be treated as categorical, not numeric.


- Docker: image = recipe + environment, container = running instance. Same code + seed gives the same metrics inside and outside.
- Copy requirements.txt before the code in a Dockerfile so the pip layer stays cached.
- Always run `git branch` before committing to check which branch you're on.