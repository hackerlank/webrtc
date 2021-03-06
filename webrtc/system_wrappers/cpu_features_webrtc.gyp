# Copyright (c) 2014 The WebRTC project authors. All Rights Reserved.
#
# Use of this source code is governed by a BSD-style license
# that can be found in the LICENSE file in the root of the source
# tree. An additional intellectual property rights grant can be found
# in the file PATENTS.  All contributing project authors may
# be found in the AUTHORS file in the root of the source tree.

{
  'includes': [ '../build/common.gypi', ],
  'conditions': [
    ['OS=="android"', {
      'targets': [
        {
          'target_name': 'cpu_features_android',
          'type': 'static_library',
          'sources': [
            'source/cpu_features_android.c',
          ],
          'dependencies': [
            # Not supported, please refer to the GN build.
            #'../../build/android/ndk.gyp:cpu_features',
          ],
        },
      ],
    }],
    ['OS=="linux"', {
      'targets': [
        {
          'target_name': 'cpu_features_linux',
          'type': 'static_library',
          'sources': [
            'source/cpu_features_linux.c',
          ],
          'dependencies': [
            '<(webrtc_root)/common.gyp:webrtc_common',
          ],
        },
      ],
    }],
  ], # conditions
}
