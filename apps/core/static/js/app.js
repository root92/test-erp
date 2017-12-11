// select the image input 
var input = document.querySelector('input[type="file"]');

// Select the image preview section
var preview = document.querySelector('.preview');

// Hide the image input Because it difficult to style 
input.style.opacity = 0;


//  add an event listener to the input to listen for changes to its selected value changes
input.addEventListener('change', updateImageDisplay);


function updateImageDisplay() {
  // Use a while loop to empty the previous contents of the preview <div	
  while(preview.firstChild) {
    preview.removeChild(preview.firstChild);
  }

  // Grab the FileList object that contains the information on all the
  //  selected files, and store it in a variable called curFiles.

  var curFiles = input.files;

  // Check to see if no files were selected, by checking ifcurFiles.length is equal to 0. 
  // If so, print a message into the preview <div> stating that no files have been selected.

  if(curFiles.length === 0) {
    var para = document.createElement('p');
    para.textContent = 'Aucun Fichier Selectioné';
    preview.appendChild(para);
  } else {
    var list = document.createElement('ol');
    preview.appendChild(list);
    for(var i = 0; i < curFiles.length; i++) {
      var listItem = document.createElement('li');
      var para = document.createElement('p');

      // check whether the file is of the correct type
       // (e.g. the image types specified in the accept attribute).

      if(validFileType(curFiles[i])) {
        para.textContent = 'Le fichier ' + curFiles[i].name + ', a une taille ' + returnFileSize(curFiles[i].size) + '.';
        var image = document.createElement('img');
        image.src = window.URL.createObjectURL(curFiles[i]);

        listItem.appendChild(image);
        listItem.appendChild(para);

      } else {
        para.textContent = 'Le fichier' + curFiles[i].name + ': n\'est pas valide. Selectionner un autre.';
        listItem.appendChild(para);
      }

      list.appendChild(listItem);
    }
  }
}

var fileTypes = [
  'image/jpeg',
  'image/pjpeg',
  'image/png'
]

function validFileType(file) {
  for(var i = 0; i < fileTypes.length; i++) {
    if(file.type === fileTypes[i]) {
      return true;
    }
  }

  return false;
}

function returnFileSize(number) {
  if(number < 1024) {
    return number + 'bytes';
  } else if(number > 1024 && number < 1048576) {
    return (number/1024).toFixed(1) + 'KB';
  } else if(number > 1048576) {
    return (number/1048576).toFixed(1) + 'MB';
  }
}


// Customizing the Html invalid message for form inputs

// select all inputs with a required Attributes 
var requireInput = document.querySelectorAll('input:required');

//Add an event listener to each input checking for invalid input and change the default message
requireInput.forEach(function(element) {
    element.oninvalid = function(event) {
    event.target.setCustomValidity('Ce champ est obligatoire');
  }
});

//Add an event listener to each input checking for  Input  and 
// remove the invalid message set previously to allow filling the form
requireInput.forEach(function(element) {
    element.oninput = function(event) {
    event.target.setCustomValidity('');
  }
});

