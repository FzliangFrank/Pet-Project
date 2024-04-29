// Function to resize the child div based on the parent div's height and width
function resizeChildDiv(parentId, childId) {
    const parentDiv = document.getElementById(parentId);
    const childDiv = document.getElementById(childId);
    let prevHeight = 0;
  
    if (parentDiv && childDiv) {
      const resizeObserver = new ResizeObserver(entries => {
        for (const entry of entries) {
          const { target } = entry;
          const parentHeight = target.offsetHeight;
  
          // Only resize child div if the parent's height changes
          if (parentHeight !== prevHeight) {
            prevHeight = parentHeight;
  
            // Resize the child div to match the parent's height and width
            childDiv.style.height = `${parentHeight}px`;
            childDiv.style.width = `${target.offsetWidth}px`;
          }// ifstatement
        }//for loop
      });
  
      // Observe changes in the height of the parent div
      resizeObserver.observe(parentDiv);
    }
  }
  
  // Usage: Call the resizeChildDiv function with the IDs of the parent and child divs
var target=document.getElementById('%s');
var cardBody=target.parentElement
var cardHead = cardBody.previousSibling
var cardTool = cardHead.getElementByClass('card-tools')
var maximizeBtn = cardTool.querySelectorAll('data-card-widget="maximize"')

let maximized=false
const ogHeight = target.offsetHeight

maximizeBtn.addEventListener('click', function(){
    if(maximized) {
        var h = cardBody.offsetHeight
        target.style.height = h + 'px'
        maximized = true
    } else {
        target.style.height = ogHeight + 'px'
    }
    
})