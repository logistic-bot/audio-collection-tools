from audio_collection_tools import *
from audio_collection_tools.generate_playlists import *

from .fixtures import *

import os

# Tests

def test_is_audio_file():
    assert is_audio_file('foo.mp3')
    assert is_audio_file('foo.MP3')
    assert is_audio_file('foo.flac')
    assert is_audio_file('foo.Flac')
    assert not is_audio_file('foo.txt')

def test_generate_pls_playlist(pls_tmpfile, audio_tmpdir):
    pl_audio_dir = os.path.relpath(audio_tmpdir, os.path.dirname(pls_tmpfile))

    generate_playlist(PlaylistSpec(pls_tmpfile, [pl_audio_dir]))

    with open(pls_tmpfile, "r") as fh:
        contents = fh.read()
        assert 'NumberOfEntries=10' in contents
        for audiofile in ['audio.m4a','audio.mp3','audio.ogg',
                          'audio.flac','audio.wav']:
            assert audiofile in contents

        for oggfile in ['{0:02d}'.format(n) + '.ogg' for n in range(1,5)]:
            assert oggfile in contents

        assert not 'notaudio.txt' in contents

def test_generate_m3u_playlist(m3u_tmpfile, audio_tmpdir):
    pl_audio_dir = os.path.relpath(audio_tmpdir, os.path.dirname(m3u_tmpfile))

    generate_playlist(PlaylistSpec(m3u_tmpfile, [pl_audio_dir]))

    with open(m3u_tmpfile, "r") as fh:
        contents = fh.read()
        for audiofile in ['audio.m4a','audio.mp3','audio.ogg',
                          'audio.flac','audio.wav']:
            assert audiofile in contents

        for oggfile in ['{0:02d}'.format(n) + '.ogg' for n in range(1,5)]:
            assert oggfile in contents

        assert not 'notaudio.txt' in contents
        
