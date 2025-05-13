
const role_mapping = {
    "show-all": "all",
    "show-data-analyst": {
        'any':["data-analyst"] },
    "show-data-engineer": {
        'any': ["data-engineer"] }
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
            const ele_tooltip = ele_tag.join(", ");
            
            element.setAttribute('title', ele_tooltip);
            element.setAttribute('data-toggle', "tooltip");
            element.setAttribute('data-placement', "left");
            element.setAttribute('tabindex', 0);


            if (tag == 'all') {
                element.style.display = "block";
                return;
            }
            let cond = true;
            if (tag.any) {
                const cond_any = tag.any.some(t => ele_tag.includes(t)) || ele_tag.includes('all')
                cond &&= cond_any;
            }
            if (tag.all) {
                const cond_all = tag.all.every(t => ele_tag.includes(t))
                cond &&= cond_all;
            }
            if (cond) {
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