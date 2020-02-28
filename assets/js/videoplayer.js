const videoContainer = document.getElementById("jsVideoPlayer");
const videoPlayer = document.querySelector("#jsVideoPlayer video")
const playBtn = document.getElementById("jsPlayButton")
const fullScrnBtn = document.getElementById("jsFullScreen")
const volumeBtn = document.getElementById("jsVolumeBtn")
const currentTime = document.getElementById("currentTime")
const totleTime = document.getElementById("totalTime")
const videoController = document.getElementById("jsVideoController")
const volumeRange = document.getElementById("jsVolumeRange")
const videoTimeRange = document.getElementById("jsVideoTimeRange")

function playVideo() {
    videoPlayer.play()
}

function handlePlayClick() {
    if (videoPlayer.paused) {
        videoPlayer.play()
        playBtn.innerHTML = '<i class="fas fa-pause"></i>'
    } else {
        videoPlayer.pause()
        playBtn.innerHTML = '<i class="fas fa-play"></i>'

    }
}
function exitFullScreen() {
    fullScrnBtn.innerHTML = '<i class="fas fa-expand"></i>'
    if (document.exitFullscreen) {
        document.exitFullscreen();
    } else if (document.mozCancelFullScreen) {
        document.mozCancelFullScreen();
    } else if (document.webkitExitFullscreen) {
        document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) {
        document.msExitFullscreen();
    }
    videoPlayer.classList.remove('xl:h-full');
    videoPlayer.classList.add('xl:h-540px');
    fullScrnBtn.addEventListener("click", goFullScreen)
}
function goFullScreen() {
    if (videoContainer.requestFullscreen) {
        videoContainer.requestFullscreen();
    } else if (videoContainer.mozRequestFullScreen) {
        videoContainer.mozRequestFullScreen();
    } else if (videoContainer.webkitRequestFullscreen) {
        videoContainer.webkitRequestFullscreen();
    } else if (videoContainer.msRequestFullscreen) {
        videoContainer.msRequestFullscreen();
    }
    videoPlayer.classList.remove('xl:h-540px');
    videoPlayer.classList.add('xl:h-full');
    fullScrnBtn.innerHTML = '<i class="fas fa-compress"></i>'
    fullScrnBtn.removeEventListener("click", goFullScreen)
    fullScrnBtn.addEventListener("click", exitFullScreen)
}
function handleVolumeClick() {
    if (videoPlayer.muted) {
        videoPlayer.muted = false;
        volumeRange.value = videoPlayer.volume
        if (videoPlayer.volume !== 0) {
            volumeBtn.innerHTML = '<i class="fas fa-volume-up"></i>'
        }
    } else {
        videoPlayer.muted = true
        volumeRange.value = 0
        volumeBtn.innerHTML = '<i class="fas fa-volume-mute"></i>'
    }
}
const formatDate = seconds => {
    const secondsNumber = parseInt(seconds, 10);
    let hours = Math.floor(secondsNumber / 3600);
    let minutes = Math.floor((secondsNumber - hours * 3600) / 60);
    let totalSeconds = secondsNumber - hours * 3600 - minutes * 60;

    if (hours < 10) {
        hours = `0${hours}`;
    }
    if (minutes < 10) {
        minutes = `0${minutes}`;
    }
    if (totalSeconds < 10) {
        totalSeconds = `0${totalSeconds}`;
    }
    if (hours == 0) {
        if (minutes == 0) {
            return `0:${totalSeconds}`;
        }
        return `${minutes}:${totalSeconds}`;
    }
    else {
        return `${hours}:${minutes}:${totalSeconds}`;
    }
}
function getCurrentTime() {
    currentTime.innerHTML = formatDate(Math.floor(videoPlayer.currentTime))
}

function setTotalTime() {
    const totalTimeString = formatDate(videoPlayer.duration);
    totalTime.innerHTML = totalTimeString;
    setInterval(getCurrentTime, 1000);
    videoTimeRange.step = 100 / videoPlayer.duration
}
function handleEnded() {
    playBtn.innerHTML = '<i class="fas fa-play"></i>'
    videoPlayer.currentTime = 0
}
function ShowController() {
    videoController.classList.remove('hidden')
    videoController.addEventListener("keydown", () => console.log("hello"))
}
function HideController() {
    if (!videoPlayer.paused) {
        videoController.classList.add('hidden');
    }
}

function handleContainerClick() {
    videoController.onclick = () => {
        event.stopPropagation();
    }
    if (videoPlayer.paused) {
        videoPlayer.play()
        playBtn.innerHTML = '<i class="fas fa-pause"></i>'
    } else {
        videoPlayer.pause()
        playBtn.innerHTML = '<i class="fas fa-play"></i>'

    }
}

function handleVolumeInput(event) {
    const { target: { value } } = event
    videoPlayer.volume = value
    if (value >= 0.5) {
        volumeBtn.innerHTML = '<i class="fas fa-volume-up"></i>'
    } else if (value > 0) {
        videoPlayer.muted = false
        volumeBtn.innerHTML = '<i class="fas fa-volume-down"></i>'
    }
    else {
        videoPlayer.muted = true
        volumeBtn.innerHTML = '<i class="fas fa-volume-mute"></i>'
    }
}

function handleVideoHeight() {
    const width = videoPlayer.offsetWidth;
    height = (width / 1.77)
    videoPlayer.style.height = `${height}px`
}
function handleKeyDown(e) {
    log.textContent += ` ${e.code}`;
}
function handleTimeUpdate() {
    videoTimeRange.value = videoPlayer.currentTime * videoTimeRange.step
}
function handleTimeRange(event) {
    const { target: { value } } = event
    if (!videoPlayer.paused) {
        videoPlayer.load()
        videoPlayer.currentTime = Math.floor(value / videoTimeRange.step)
        videoPlayer.play()
    } else {
        videoPlayer.load()
        videoPlayer.currentTime = Math.floor(value / videoTimeRange.step)
    }

}

function init() {
    videoPlayer.volume = "0.5"
    videoPlayer.load()
    window.addEventListener("resize", handleVideoHeight)
    videoPlayer.addEventListener("loadedmetadata", setTotalTime)
    videoContainer.addEventListener("mouseover", ShowController)
    videoContainer.addEventListener("mouseout", HideController)
    videoContainer.addEventListener("click", handleContainerClick)
    playBtn.addEventListener("click", handlePlayClick)
    fullScrnBtn.addEventListener("click", goFullScreen)
    volumeBtn.addEventListener("click", handleVolumeClick)
    videoPlayer.addEventListener("ended", handleEnded)
    volumeRange.addEventListener("input", handleVolumeInput)
    videoPlayer.addEventListener("timeupdate", handleTimeUpdate)
    videoTimeRange.addEventListener("input", handleTimeRange)
}

if (videoContainer) {
    init()
}