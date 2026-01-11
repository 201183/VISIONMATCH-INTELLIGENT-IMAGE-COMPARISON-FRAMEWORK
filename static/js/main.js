// Form validation for login and registration
document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');
    const compareForm = document.getElementById('compareForm');

    if (loginForm) {
        loginForm.addEventListener('submit', function (e) {
            const username = document.querySelector('input[name="username"]').value;
            const password = document.querySelector('input[name="password"]').value;

            if (!username || !password) {
                e.preventDefault();
                alert('Please fill in all fields.');
            }
        });
    }

    if (registerForm) {
        registerForm.addEventListener('submit', function (e) {
            const username = document.querySelector('input[name="username"]').value;
            const password = document.querySelector('input[name="password"]').value;

            if (!username || !password) {
                e.preventDefault();
                alert('Please fill in all fields.');
            }
        });
    }

    // File preview and loading spinner for compare page
    if (compareForm) {
        const image1Input = document.getElementById('image1');
        const image2Input = document.getElementById('image2');
        const preview1 = document.getElementById('preview1');
        const preview2 = document.getElementById('preview2');
        const loading = document.getElementById('loading');

        if (image1Input && preview1) {
            image1Input.addEventListener('change', function (e) {
                const file = e.target.files[0];
                if (file) {
                    preview1.src = URL.createObjectURL(file);
                    preview1.style.display = 'block';
                }
            });
        }

        if (image2Input && preview2) {
            image2Input.addEventListener('change', function (e) {
                const file = e.target.files[0];
                if (file) {
                    preview2.src = URL.createObjectURL(file);
                    preview2.style.display = 'block';
                }
            });
        }

        compareForm.addEventListener('submit', function () {
            if (loading) {
                loading.style.display = 'block';
            }
        });
    }

    // Table sorting for history page
    const historyTable = document.getElementById('historyTable');
    if (historyTable) {
        const headers = historyTable.querySelectorAll('th');
        headers.forEach((header, index) => {
            header.addEventListener('click', () => sortTable(index));
        });
    }
});

// Sort table by column
function sortTable(column) {
    const table = document.getElementById('historyTable');
    const rows = Array.from(table.querySelectorAll('tbody tr'));
    const isAsc = table.rows[0].cells[column].classList.toggle('asc');

    rows.sort((a, b) => {
        const aVal = a.cells[column].textContent;
        const bVal = b.cells[column].textContent;
        return isAsc ? aVal.localeCompare(bVal) : bVal.localeCompare(aVal);
    });

    rows.forEach(row => table.tBodies[0].appendChild(row));
}