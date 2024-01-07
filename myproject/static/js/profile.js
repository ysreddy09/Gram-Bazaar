document.getElementById('changePhoto').addEventListener('change', function (event) {
      const file = event.target.files[0];
      const reader = new FileReader();

      reader.onload = function (e) {
        const profileImg = document.getElementById('profileImage');
        profileImg.querySelector('img').src = e.target.result;
      };

      reader.readAsDataURL(file);
    });

    document.getElementById('removePhoto').addEventListener('click', function () {
      const defaultImageSrc = 'path/to/default_image.jpg'; // Replace with your default image path
      const profileImg = document.getElementById('profileImage');
      profileImg.querySelector('img').src = defaultImageSrc;
    });
