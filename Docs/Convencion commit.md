# Convención de Commits
## Formato del Commit

```plaintext
<tipo>(<ámbito>): <mensaje>
```

### Tipos de Commit

- **feat:** Nuevas características.
  - Añadir nuevas funcionalidades o características al código.
  - **Ejemplo:**
    ```plaintext
    feat(login): agregar función de inicio de sesión con OAuth
    ```
- **fix:** Corrección de errores.
  - Solucionar bugs que afectan el funcionamiento del código.
  - **Ejemplo:**
    ```plaintext
    fix(api): solucionar error de manejo de archivos que causaba un bloqueo
    ```
- **docs:** Cambios en la documentación.
  - Actualizar o mejorar la documentación, tanto del código como externa.
  - **Ejemplo:**
    ```plaintext
    docs(readme): agregar sección de instalación
    ```
- **style:** Cambios que no afectan el significado del código (espacios en blanco, formato, etc.).
  - Formateo de código (e.g., ajuste de indentación).
  - Eliminación de espacios en blanco innecesarios.
  - Corrección de nombres de variables o funciones para seguir convenciones de estilo.
  - Reorganización de imports.
  - **Ejemplo:**
    ```plaintext
    style(ui): ajustar indentación y eliminar espacios en blanco innecesarios
    ```
- **refactor:** Refactorización del código existente.
  - Mejorar la estructura del código sin cambiar su funcionalidad.
  - Simplificar el código.
  - **Ejemplo:**
    ```plaintext
    refactor(auth): simplificar la lógica de autenticación
    ```
- **test:** Añadir o modificar pruebas.
  - Crear nuevas pruebas o actualizar las existentes.
  - **Ejemplo:**
    ```plaintext
    test(profile): agregar pruebas unitarias para la función de actualización de perfil
    ```
- **chore:** Tareas diversas que no se incluyen en los tipos anteriores.
  - Actualización de dependencias.
  - Eliminación de funciones o archivos obsoletos que no afectan la funcionalidad del código.
  - **Ejemplo:**
    ```plaintext
    chore(deps): actualizar dependencias a sus versiones más recientes
    ```
  - **Ejemplo:**
    ```plaintext
    chore(cleanup): eliminar funciones obsoletas del módulo de autenticación
    ```

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


## Diferenciando Tipos de Commit

- **feat:** Utiliza `feat` para agregar nuevas funcionalidades o características.
  - **Ejemplo:**
    ```plaintext
    feat(dashboard): agregar gráficos interactivos al panel de control
    ```

- **fix:** Utiliza `fix` cuando el cambio corrige un error que afecta el comportamiento del código o la lógica de la aplicación.
  - **Ejemplo:**
    ```plaintext
    fix(login): corregir validación incorrecta de contraseñas
    ```

- **docs:** Utiliza `docs` para cualquier cambio en la documentación, como guías, manuales o comentarios en el código.
  - **Ejemplo:**
    ```plaintext
    docs(api): actualizar la documentación del endpoint de usuarios
    ```

- **style:** Utiliza `style` para cambios que no afectan la funcionalidad del código, sino que mejoran su apariencia o adherencia a las convenciones de estilo.
  - **Ejemplo:**
    ```plaintext
    style(auth): cambiar nombre de variables para seguir convención camelCase
    ```

- **refactor:** Utiliza `refactor` para mejorar la estructura del código sin cambiar su funcionalidad.
  - **Ejemplo:**
    ```plaintext
    refactor(controller): modularizar el controlador de usuarios
    ```

- **test:** Utiliza `test` para añadir o modificar pruebas de código.
  - **Ejemplo:**
    ```plaintext
    test(api): añadir pruebas de integración para el endpoint de creación de usuarios
    ```

- **chore:** Utiliza `chore` para tareas de mantenimiento que no afectan la funcionalidad del código.
  - **Ejemplo:**
    ```plaintext
    chore(deps): actualizar dependencias de npm
    ```

## Reglas Adicionales

- Mantén los mensajes en tiempo presente.
- Limita la longitud de la línea a 72 caracteres.
- Usa un imperativo en el mensaje.
- Especifica el ámbito para contextualizar el cambio.
