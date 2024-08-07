document.addEventListener('DOMContentLoaded', (event) => {
    const itemInput = document.getElementById('itemInput');
    const addItemButton = document.getElementById('addItemButton');
    const itemList = document.getElementById('itemList');

    addItemButton.addEventListener('click', () => {
        const newItemText = itemInput.value.trim();
        if (newItemText !== '') {
            const listItem = document.createElement('li');
            listItem.textContent = newItemText;
            itemList.appendChild(listItem);
            itemInput.value = '';
        }
    });

    // 使输入框在按下 Enter 键时也能添加项目
    itemInput.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            addItemButton.click();
        }
    });
});
