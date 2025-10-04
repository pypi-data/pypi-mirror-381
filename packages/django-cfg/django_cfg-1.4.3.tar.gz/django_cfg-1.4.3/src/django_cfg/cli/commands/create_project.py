"""
Django CFG Create Project Command

Creates a new Django project by downloading from GitHub.
"""

import click
import shutil
import urllib.request
from pathlib import Path
import tempfile
import zipfile

# GitHub template URL
TEMPLATE_URL = "https://github.com/markolofsen/django-cfg/archive/refs/heads/main.zip"


def download_template(url: str) -> Path:
    """Download template archive from GitHub."""
    click.echo("📥 Downloading template from GitHub...")

    try:
        # Create temp file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.zip')
        temp_path = Path(temp_file.name)

        # Download with progress
        with urllib.request.urlopen(url) as response:
            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0
            chunk_size = 8192

            with open(temp_path, 'wb') as f:
                while True:
                    chunk = response.read(chunk_size)
                    if not chunk:
                        break
                    f.write(chunk)
                    downloaded += len(chunk)

                    if total_size > 0:
                        progress = (downloaded / total_size) * 100
                        click.echo(f"\r   Progress: {progress:.1f}%", nl=False)

        click.echo("\n✅ Template downloaded successfully")
        return temp_path

    except Exception as e:
        raise RuntimeError(f"Failed to download template: {e}")


def extract_template(archive_path: Path, target_path: Path) -> None:
    """Extract template archive to target directory."""
    click.echo("📂 Extracting template...")

    try:
        with zipfile.ZipFile(archive_path, 'r') as archive:
            members = archive.namelist()

            # Find the root folder name (django-cfg-main)
            root_folder = members[0].split('/')[0] if members else None

            if not root_folder:
                raise ValueError("Archive structure is invalid")

            # Path to django project in archive: django-cfg-main/libs/django_cfg_example/django/
            template_prefix = f"{root_folder}/libs/django_cfg_example/django/"

            # Extract only files from the django/ folder
            extracted_files = 0
            for member in members:
                # Skip if not in template path
                if not member.startswith(template_prefix):
                    continue

                # Skip the django_cfg folder (local package)
                if f"{root_folder}/libs/django_cfg_example/django_cfg/" in member:
                    continue

                # Calculate relative path (remove template_prefix)
                relative_path = member[len(template_prefix):]

                # Skip empty paths (directory markers)
                if not relative_path:
                    continue

                # Target file path
                target_file = target_path / relative_path

                # Extract file
                if member.endswith('/'):
                    # Create directory
                    target_file.mkdir(parents=True, exist_ok=True)
                else:
                    # Create parent directories
                    target_file.parent.mkdir(parents=True, exist_ok=True)

                    # Extract file content
                    with archive.open(member) as source:
                        with open(target_file, 'wb') as target:
                            target.write(source.read())

                    extracted_files += 1

        click.echo(f"✅ Template extracted successfully ({extracted_files} files)")

    except zipfile.BadZipFile:
        raise ValueError(f"Invalid template archive")
    except Exception as e:
        raise RuntimeError(f"Failed to extract template: {e}")


@click.command()
@click.option(
    "--path",
    "-p",
    type=click.Path(),
    default=".",
    help="Directory where to create the project (default: current directory)"
)
@click.option(
    "--force",
    "-f",
    is_flag=True,
    help="Overwrite existing files if they exist"
)
def create_project(path: str, force: bool):
    """
    🚀 Create a new Django project with django-cfg

    Downloads the latest django-cfg template from GitHub and extracts it.

    Examples:

        # Extract to current directory
        django-cfg create-project

        # Extract to specific directory
        django-cfg create-project --path ./my-project/

        # Overwrite existing files
        django-cfg create-project --force
    """

    # Determine target path
    target_path = Path(path).resolve()

    # Check if target directory exists and has files
    if target_path.exists() and any(target_path.iterdir()):
        if not force:
            click.echo(f"❌ Directory '{target_path}' is not empty. Use --force to overwrite.", err=True)
            return
        else:
            click.echo(f"⚠️  Directory is not empty, files will be overwritten...")

    temp_archive = None

    try:
        click.echo(f"🚀 Creating Django project from GitHub")
        click.echo(f"📁 Target location: {target_path}")
        click.echo()

        # Download template from GitHub
        temp_archive = download_template(TEMPLATE_URL)

        # Create target directory
        target_path.mkdir(parents=True, exist_ok=True)

        # Extract template
        extract_template(temp_archive, target_path)

        click.echo()
        click.echo(f"✅ Project created successfully!")
        click.echo(f"📁 Location: {target_path}")

        # Show next steps
        click.echo()
        click.echo("📋 Next steps:")
        if target_path != Path.cwd():
            click.echo(f"   cd {target_path}")
        click.echo("   poetry install  # or: pip install -r requirements.txt")
        click.echo("   python manage.py migrate")
        click.echo("   python manage.py createsuperuser")
        click.echo("   python manage.py runserver")

        click.echo()
        click.echo("💡 Features included:")
        click.echo("   🔧 Type-safe configuration with Pydantic v2")
        click.echo("   📱 Twilio integration (WhatsApp, SMS, Email OTP)")
        click.echo("   📧 Email services with SendGrid")
        click.echo("   💬 Telegram bot integration")
        click.echo("   🎨 Modern Unfold admin interface")
        click.echo("   📊 Auto-generated API documentation")
        click.echo("   🔐 JWT authentication system")
        click.echo("   🗃️ Multi-database support with routing")
        click.echo("   ⚡ Background task processing")
        click.echo("   🐳 Docker deployment ready")

        click.echo()
        click.echo("📚 Documentation: https://github.com/markolofsen/django-cfg")
        click.echo("🌐 Developed by Unrealon.com — Complex parsers on demand")

    except Exception as e:
        click.echo(f"❌ Error creating project: {e}", err=True)
        # Clean up on error
        if target_path.exists():
            shutil.rmtree(target_path, ignore_errors=True)
        raise

    finally:
        # Clean up temp file
        if temp_archive and temp_archive.exists():
            temp_archive.unlink()
