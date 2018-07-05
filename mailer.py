import os
os.system('echo "$(date) Un simple texto para validar que funciona correctamente un post-commit" | mail -s "Correo enviado desde hook post-commit by-python" root@lab.example.com')
