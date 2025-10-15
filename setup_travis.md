# Travis CI Setup Guide

## Prerequisites
1. Your Django project is pushed to GitHub
2. You have a GitHub account
3. You have an AWS account (for Elastic Beanstalk deployment)

## Step 1: Connect Travis CI to GitHub

1. Go to [Travis CI](https://travis-ci.com/)
2. Sign in with your GitHub account
3. Click "Activate" to enable Travis CI for your repositories
4. Find your repository in the list and toggle it ON

## Step 2: Update .travis.yml with your specific details

You need to update the following placeholders in `.travis.yml`:

```yaml
deploy:
  provider: elasticbeanstalk
  region: us-east-1  # Change to your AWS region
  app: your-app-name  # Your EB application name
  env: your-app-env   # Your EB environment name
  bucket_name: your-eb-bucket  # Your EB S3 bucket name
```

## Step 3: Set up AWS Elastic Beanstalk (if not already done)

1. Go to AWS Elastic Beanstalk console
2. Create a new application (if you don't have one)
3. Create a new environment for your Django app
4. Note down:
   - Application name
   - Environment name
   - Region
   - S3 bucket name

## Step 4: Set up AWS credentials in Travis CI

1. In Travis CI, go to your repository settings
2. Add these environment variables:
   - `AWS_ACCESS_KEY_ID`: Your AWS access key
   - `AWS_SECRET_ACCESS_KEY`: Your AWS secret key

## Step 5: Set up Coveralls

1. Go to [Coveralls.io](https://coveralls.io/)
2. Sign in with GitHub
3. Add your repository
4. Get your repository token
5. Add `COVERALLS_REPO_TOKEN` to Travis CI environment variables

## Step 6: Update README.md badges

Replace the placeholders in `README.md`:
- `YOUR_GITHUB_USERNAME`: Your GitHub username
- `YOUR_REPO_NAME`: Your repository name
- Update the deployed application URL

## Step 7: Set up GitHub Branch Protection

1. Go to your GitHub repository
2. Click "Settings" → "Branches"
3. Click "Add rule"
4. Set branch name pattern to `main` (or `master`)
5. Check "Require status checks to pass before merging"
6. Select "Travis CI - Branch" and "Travis CI - Pull Request"
7. Click "Create"

## Step 8: Test the setup

1. Make a small change to your code
2. Push to GitHub
3. Check Travis CI dashboard to see the build
4. Create a pull request to test the branch protection

## Troubleshooting

### Common Issues:

1. **Build fails due to formatting**: Run `black .` locally and commit
2. **Build fails due to linting**: Fix flake8 issues and commit
3. **Tests fail**: Check your test cases and fix any issues
4. **Deployment fails**: Verify AWS credentials and EB configuration

### Local Testing Commands:

```bash
# Activate virtual environment
source venv/bin/activate

# Check formatting
black --check .

# Run linter
flake8 .

# Run tests with coverage
coverage run --source='.' manage.py test
coverage report

# Format code (if needed)
black .
```

## Files Created/Modified:

- `.travis.yml` - Travis CI configuration
- `.flake8` - Flake8 linting configuration
- `.coveragerc` - Coverage.py configuration
- `requirements.txt` - Updated with CI/CD dependencies
- `README.md` - Added badges and documentation
- `polls/tests.py` - Added basic tests

## Next Steps:

1. Push all changes to GitHub
2. Set up Travis CI as described above
3. Configure AWS credentials
4. Test with a pull request
5. Submit your working URLs as required
