
const role_mapping = {
    "show-all": "all",
    "show-data-analyst": "data-analyst",
    "show-data-engineer": "data-engineer"
}
// Main event handler
const handleRadioChange = async (event) => {
    if (event.target.checked) {
        const target_id = event.target.id;
        const tag = role_mapping[target_id];
        // console.log(target_id);
        document.querySelectorAll('div.taged-item').forEach(element => {
            const ele_tag_str = element.dataset.tags;
            const ele_tag = JSON.parse(ele_tag_str.replace(/'/g, '"'));

            if (tag == 'all') {
                element.style.display = "block";
                return;
            }
            if (ele_tag.includes(tag) || ele_tag.includes('all') ) {
                console.log(ele_tag);
                element.style.display = "block";
            } else {
                element.style.display = "none";
            }
        });
    }
};

// Initialize radio buttons
const initializeRadioButtons = () => {
    const radioButtons = document.querySelectorAll('#role-selector .btn-check');
    radioButtons.forEach(radio => {
        radio.addEventListener('change', handleRadioChange);
    });
};

// Start the application
document.addEventListener('DOMContentLoaded', initializeRadioButtons);