document.addEventListener('DOMContentLoaded', function () {
    const playPauseButtons = document.querySelectorAll('.play-pause-btn');
    
    let currentlyPlayingAudio = null; // To track the currently playing or paused audio
    let currentlyPlayingItem = null;  // To track the currently expanded audio item
    let currentlyPlayingButton = null;  // To track the play/pause button of the current audio

    playPauseButtons.forEach(function(button) {
        const audioItem = button.closest('.audio-item');
        const audioPlayer = audioItem.querySelector('.audioPlayer');
        const progressBar = audioItem.querySelector('.progress-bar');
        const songInfo = audioItem.querySelector('.song-info'); // Reference to the song info element

        button.addEventListener('click', function () {
            if (audioPlayer.paused) {
                // If another audio is playing or paused, reset it
                if (currentlyPlayingAudio && currentlyPlayingAudio !== audioPlayer) {
                    currentlyPlayingAudio.pause(); // Pause the other audio
                    currentlyPlayingButton.src = currentlyPlayingButton.getAttribute('audio-play');
                    currentlyPlayingItem.classList.remove('expanded');
                    const previousProgressBar = currentlyPlayingItem.querySelector('.progress-bar');
                    previousProgressBar.value = 0;
                    const previousSongInfo = currentlyPlayingItem.querySelector('.song-info');
                    previousSongInfo.textContent = ""; // Clear song info
                }

                // Play the clicked audio
                audioPlayer.play();
                button.src = button.getAttribute('audio-pause');
                audioItem.classList.add('expanded'); // Expand the audio item and show progress bar and song info

                // Update the current and total duration in song info
                audioPlayer.addEventListener('loadedmetadata', function() {
                    const duration = formatTime(audioPlayer.duration);
                    songInfo.textContent = `00:00 / ${duration}`;
                });

                // Update progress bar and current time during playback
                audioPlayer.addEventListener('timeupdate', function () {
                    const progress = (audioPlayer.currentTime / audioPlayer.duration) * 100;
                    progressBar.value = progress;
                    const currentTime = formatTime(audioPlayer.currentTime);
                    const duration = formatTime(audioPlayer.duration);
                    songInfo.textContent = `${currentTime} / ${duration}`;
                });

                currentlyPlayingAudio = audioPlayer;
                currentlyPlayingItem = audioItem;
                currentlyPlayingButton = button;

            } else {
                // Pause the audio and keep progress and song info visible
                audioPlayer.pause();
                button.src = button.getAttribute('audio-play');
                audioItem.classList.add('expanded'); // Keep the progress bar and song info when paused

                // Keep the progress bar and song info at the current state
                const progress = (audioPlayer.currentTime / audioPlayer.duration) * 100;
                progressBar.value = progress;
                const currentTime = formatTime(audioPlayer.currentTime);
                const duration = formatTime(audioPlayer.duration);
                songInfo.textContent = `${currentTime} / ${duration}`;
            }
        });

        // Reset button and progress bar when the audio ends
        audioPlayer.addEventListener('ended', function () {
            button.src = button.getAttribute('audio-play');
            audioItem.classList.remove('expanded'); // Collapse the audio item
            progressBar.value = 0; // Reset progress bar
            songInfo.textContent = ""; // Clear song info
            currentlyPlayingAudio = null; // No active audio after ending
            currentlyPlayingItem = null;
            currentlyPlayingButton = null;
        });
    });

    // Function to format time in minutes and seconds
    function formatTime(seconds) {
        const minutes = Math.floor(seconds / 60);
        const secs = Math.floor(seconds % 60);
        return `${minutes}:${secs < 10 ? '0' : ''}${secs}`; // Add leading zero if seconds < 10
    }
});
