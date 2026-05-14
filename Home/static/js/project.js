function toggleCase(id) {
    const all = document.querySelectorAll('.case-hidden');

    all.forEach(item => {
        item.style.display = 'none';
    });

    const selected = document.getElementById(id);

    if (selected) {
        selected.style.display = 'block';
    }
}