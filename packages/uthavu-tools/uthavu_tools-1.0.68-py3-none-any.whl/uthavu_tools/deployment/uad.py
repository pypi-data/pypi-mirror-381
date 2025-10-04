import subprocess
import click

@click.command()
@click.option("--host", default="root@srv1014288", help="SSH host (e.g. user@ip)")
@click.option("--path", default="/var/www/adangal", help="Path to app repo on server")
@click.option("--service", default="adangal-api", help="Backend systemd service name")
@click.option("--frontend", is_flag=True, help="Also deploy frontend (npm build)")
def main(host, path, service, frontend):
    """
    Auto Update & Deploy (AUD)
    SSH into server, pull latest code and restart services.
    """
    # Base deploy commands
    commands = [
        f"cd {path}",
        "git fetch origin main",
        "git reset --hard origin/main",
        f"pip install -r requirements.txt",
        f"systemctl restart {service}"
    ]

    # Add frontend steps if requested
    if frontend:
        commands.insert(3, "npm install --omit=dev && npm run build && pm2 restart adangal-frontend")

    # Join commands into one shell script
    remote_cmd = " && ".join(commands)

    click.echo(f"🚀 Deploying on {host}:{path}")
    try:
        subprocess.run(["ssh", host, remote_cmd], check=True)
        click.echo("✅ Deployment complete")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Deployment failed: {e}")
