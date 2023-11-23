# Convención de Commits
## Formato del Commit

```plaintext
<tipo>(<ámbito>): <mensaje>
```

### Tipos de Commit

- **feat:** Nuevas características.
- **fix:** Corrección de errores.
- **docs:** Cambios en la documentación.
- **style:** Cambios que no afectan el significado del código (espacios en blanco, formato, etc.).
- **refactor:** Refactorización del código existente.
- **test:** Añadir o modificar pruebas.
- **chore:** Tareas diversas que no se incluyen en los tipos anteriores.

## Ámbitos Sugeridos:

1. **Módulo o Componente:**
   - `auth`: Cambios relacionados con la autenticación.
   - `ui`: Modificaciones en la interfaz de usuario.
   - `api`: Afecta a la capa de servicios o API.

2. **Funcionalidad Específica:**
   - `login`: Cambios específicos en el inicio de sesión.
   - `profile`: Modificaciones en la sección de perfil.
   - `dashboard`: Afecta al panel de control.

3. **Ubicación Geográfica:**
   - `frontend`: Cambios en el frontend.
   - `backend`: Modificaciones en el backend.
   - `db`: Relacionado con la base de datos.

4. **Nivel de Abstracción:**
   - `model`: Cambios en la lógica de datos o modelos.
   - `view`: Afecta a la capa de presentación.
   - `controller`: Modificaciones en controladores.

5. **Contexto Específico:**
   - `testing`: Cambios relacionados con pruebas.
   - `docs`: Modificaciones en la documentación.


## Ejemplos

### Nuevo Feature

```plaintext
feat(login): agregar función de inicio de sesión
```

### Corrección de Error

```plaintext
fix(api): solucionar error de manejo de archivos
```

## Reglas Adicionales

- Mantén los mensajes en tiempo presente.
- Limita la longitud de la línea a 72 caracteres.
- Usa un imperativo en el mensaje.
- Especifica el ámbito para contextualizar el cambio.
