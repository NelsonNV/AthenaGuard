$(document).ready(function() {
    $('table').DataTable({
        "language": {
            "url": "https://cdn.datatables.net/plug-ins/1.13.5/i18n/es-ES.json"
        },
        "dom": '<"flex justify-between items-center mb-4"lf>t<"flex justify-between items-center mt-4"ip>',
        "pagingType": "simple_numbers", // Estilo más compacto para la paginación
        "initComplete": function() {
            // Añade clases de Tailwind a los elementos de DataTables
            $('div.dataTables_filter input').addClass('bg-gray-800 text-gray-300 border border-gray-700 rounded-lg px-4 py-2');
            $('div.dataTables_length select option').addClass('bg-gray-800 text-gray-300 border border-gray-700 rounded-lg px-4 py-2');
            $('div.dataTables_paginate').addClass('text-gray-300');
            $('div.dataTables_info').addClass('text-gray-400');

            // Añade clases a los botones de paginación
            $('div.dataTables_paginate a').addClass('text-gray-300 hover:text-white');
            $('div.dataTables_paginate .paginate_button.current').addClass('bg-indigo-600 text-white');

            // Añade clases de margen/padding a las filas (<tr>) y celdas (<td>)
            $('table.dataTable tbody tr').addClass('hover:bg-gray-700');
            $('table.dataTable tbody tr td').addClass('px-6 py-4'); // Padding horizontal y vertical
        }
    });
});
