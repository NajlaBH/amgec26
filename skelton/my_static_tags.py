   # skelton/templatetags/my_static_tags.py
    import os
    from django import template
    from django.conf import settings

    register = template.Library()

    @register.simple_tag
    def get_css_files_from_folder(folder_name):
        css_files = []
        static_root = settings.STATIC_ROOT if settings.STATIC_ROOT else settings.BASE_DIR / 'static' # Adjust based on your setup
        css_folder_path = os.path.join(static_root, folder_name)

        if os.path.exists(css_folder_path) and os.path.isdir(css_folder_path):
            for filename in os.listdir(css_folder_path):
                if filename.endswith('.css'):
                    css_files.append(os.path.join(folder_name, filename))
        return css_files