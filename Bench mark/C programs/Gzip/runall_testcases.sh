#!/usr/bin/sh

echo ">>>>>>>>running test 1"
../source/allfile.exe -h  >&    ../outputs/t1

echo ">>>>>>>>running test 2"
../source/allfile.exe --help  >&    ../outputs/t2

echo ">>>>>>>>running test 3"
../source/allfile.exe -L  >&    ../outputs/t3

echo ">>>>>>>>running test 4"
../source/allfile.exe --license  >&    ../outputs/t4

echo ">>>>>>>>running test 5"
../source/allfile.exe -V <   ../inputs/ >&    ../outputs/t5

echo ">>>>>>>>running test 6"
../source/allfile.exe --version <   ../inputs/ >&    ../outputs/t6

echo ">>>>>>>>running test 7"
../source/allfile.exe ../inputs/testdir/file26 -c  >&    ../outputs/t7

echo ">>>>>>>>running test 8"
../source/allfile.exe --stdout <   ../inputs/testdir/file27 >&    ../outputs/t8

echo ">>>>>>>>running test 9"
../source/allfile.exe -d <   ../inputs/gzdir/file8.z >&    ../outputs/t9

echo ">>>>>>>>running test 10"
../source/allfile.exe ../inputs/gzdir/file9.z -d  >&    ../outputs/t10
../../testplans.alt/testscripts/cpoptd.sh

echo ">>>>>>>>running test 11"
../source/allfile.exe --decompress <   ../inputs/gzdir/file5.z >&    ../outputs/t11

echo ">>>>>>>>running test 12"
../source/allfile.exe --uncompress <   ../inputs/gzdir/file6.z >&    ../outputs/t12

echo ">>>>>>>>running test 13"
../source/allfile.exe ../inputs/testdir/file3 -f  >&    ../outputs/t13
../../testplans.alt/testscripts/cpoptf.sh

echo ">>>>>>>>running test 14"
../source/allfile.exe --force <   ../inputs/testdir/file4 >&    ../outputs/t14

echo ">>>>>>>>running test 15"
../source/allfile.exe ../inputs/testdir/file32 -q  >&    ../outputs/t15
../../testplans.alt/testscripts/cpoptq.sh

echo ">>>>>>>>running test 16"
../source/allfile.exe --quiet <   ../inputs/testdir/file10 >&    ../outputs/t16

echo ">>>>>>>>running test 17"
../source/allfile.exe -r ../inputs/testdir/subdir1  >&    ../outputs/t17
../../testplans.alt/testscripts/cpoptr1.sh

echo ">>>>>>>>running test 18"
../source/allfile.exe ../inputs/testdir/subdir2 -r  >&    ../outputs/t18
../../testplans.alt/testscripts/cpoptr.sh

echo ">>>>>>>>running test 19"
../source/allfile.exe --recurse ../inputs/testdir/subdir3  >&    ../outputs/t19
../../testplans.alt/testscripts/cpoptr2.sh

echo ">>>>>>>>running test 20"
../source/allfile.exe -t <   ../inputs/gzdir/file1.z >&    ../outputs/t20

echo ">>>>>>>>running test 21"
../source/allfile.exe ../inputs/gzdir/file1.z -t  >&    ../outputs/t21

echo ">>>>>>>>running test 22"
../source/allfile.exe --test <   ../inputs/gzdir/file1.z >&    ../outputs/t22

echo ">>>>>>>>running test 23"
../source/allfile.exe ../inputs/testdir/file11 -v  >&    ../outputs/t23
../../testplans.alt/testscripts/cpoptv.sh

echo ">>>>>>>>running test 24"
../source/allfile.exe --verbose <   ../inputs/testdir/file12 >&    ../outputs/t24

echo ">>>>>>>>running test 25"
../source/allfile.exe ../inputs/testdir/file13 -1  >&    ../outputs/t25
  ../../testplans.alt/testscripts/cpopt1.sh

echo ">>>>>>>>running test 26"
../source/allfile.exe --fast <   ../inputs/testdir/file14 >&    ../outputs/t26

echo ">>>>>>>>running test 27"
../source/allfile.exe ../inputs/testdir/file15 -2  >&    ../outputs/t27
  ../../testplans.alt/testscripts/cpopt2.sh

echo ">>>>>>>>running test 28"
../source/allfile.exe ../inputs/testdir/file16 -3  >&    ../outputs/t28
  ../../testplans.alt/testscripts/cpopt3.sh

echo ">>>>>>>>running test 29"
../source/allfile.exe ../inputs/testdir/file17 -4  >&    ../outputs/t29
  ../../testplans.alt/testscripts/cpopt4.sh

echo ">>>>>>>>running test 30"
../source/allfile.exe ../inputs/testdir/file18 -5  >&    ../outputs/t30
  ../../testplans.alt/testscripts/cpopt5.sh

echo ">>>>>>>>running test 31"
../source/allfile.exe ../inputs/testdir/file19 -6  >&    ../outputs/t31
  ../../testplans.alt/testscripts/cpopt6.sh

echo ">>>>>>>>running test 32"
../source/allfile.exe ../inputs/testdir/file20 -7  >&    ../outputs/t32
  ../../testplans.alt/testscripts/cpopt7.sh

echo ">>>>>>>>running test 33"
../source/allfile.exe ../inputs/testdir/file21 -8  >&    ../outputs/t33
  ../../testplans.alt/testscripts/cpopt8.sh

echo ">>>>>>>>running test 34"
../source/allfile.exe ../inputs/testdir/file22 -9  >&    ../outputs/t34
  ../../testplans.alt/testscripts/cpopt9.sh

echo ">>>>>>>>running test 35"
../source/allfile.exe --best <   ../inputs/testdir/file23 >&    ../outputs/t35

echo ">>>>>>>>running test 36"
../source/allfile.exe <   ../inputs/testdir/subdir >&    ../outputs/t36

echo ">>>>>>>>running test 37"
../source/allfile.exe <   ../inputs/testdir/zerobytefile >&    ../outputs/t37

echo ">>>>>>>>running test 38"
../source/allfile.exe -d <   ../inputs/gzdir/corruptfile.z >&    ../outputs/t38

echo ">>>>>>>>running test 39"
../source/allfile.exe <   ../inputs/gzdir/zfile.z >&    ../outputs/t39

echo ">>>>>>>>running test 40"
../source/allfile.exe -d <   ../inputs/gzdir/zipfile.zip >&    ../outputs/t40

echo ">>>>>>>>running test 41"
../source/allfile.exe -d <   ../inputs/gzdir/compressfile.Z >&    ../outputs/t41

echo ">>>>>>>>running test 42"
../source/allfile.exe -d <   ../inputs/gzdir/pkzipfile.Z >&    ../outputs/t42

echo ">>>>>>>>running test 43"
../source/allfile.exe -d <   ../inputs/gzdir/packfile.z >&    ../outputs/t43

echo ">>>>>>>>running test 44"
../source/allfile.exe <   ../inputs/testdir/symbolicfile >&    ../outputs/t44

echo ">>>>>>>>running test 45"
../source/allfile.exe <   ../inputs/testdir/file4 >&    ../outputs/t45

echo ">>>>>>>>running test 46"
../source/allfile.exe <   ../inputs/testdir/binaryfile0 >&    ../outputs/t46

echo ">>>>>>>>running test 47"
../source/allfile.exe -d <   ../inputs/gzdir/file101.z >&    ../outputs/t47

echo ">>>>>>>>running test 48"
../source/allfile.exe <   ../inputs/testdir/encryptfile >&    ../outputs/t48

echo ">>>>>>>>running test 49"
../source/allfile.exe -d <   ../inputs/gzdir/encryptfile1.z >&    ../outputs/t49

echo ">>>>>>>>running test 50"
../source/allfile.exe -d <   ../inputs/gzdir/errorfile.z >&    ../outputs/t50


echo ">>>>>>>>running test 51"
../source/allfile.exe <   ../inputs/testdir/tarfile.tar >&    ../outputs/t51

echo ">>>>>>>>running test 52"
../source/allfile.exe -d <   ../inputs/gzdir/tarfile.tgz >&    ../outputs/t52


echo ">>>>>>>>running test 53"
../source/allfile.exe -fqrv1 <   ../inputs/testdir/file2 >&    ../outputs/t53

echo ">>>>>>>>running test 54"
../source/allfile.exe -fqrv2 <   ../inputs/testdir/file2 >&    ../outputs/t54

echo ">>>>>>>>running test 55"
../source/allfile.exe -fqrv3 <   ../inputs/testdir/file2 >&    ../outputs/t55

echo ">>>>>>>>running test 56"
../source/allfile.exe -fqrv4 <   ../inputs/testdir/file2 >&    ../outputs/t56

echo ">>>>>>>>running test 57"
../source/allfile.exe -fqrv5 <   ../inputs/testdir/file2 >&    ../outputs/t57

echo ">>>>>>>>running test 58"
../source/allfile.exe -fqrv6 <   ../inputs/testdir/file2 >&    ../outputs/t58

echo ">>>>>>>>running test 59"
../source/allfile.exe -fqrv7 <   ../inputs/testdir/file2 >&    ../outputs/t59

echo ">>>>>>>>running test 60"
../source/allfile.exe -fqrv8 <   ../inputs/testdir/file2 >&    ../outputs/t60

echo ">>>>>>>>running test 61"
../source/allfile.exe -fqrv9 <   ../inputs/testdir/file2 >&    ../outputs/t61

echo ">>>>>>>>running test 62"
../source/allfile.exe -fqrv <   ../inputs/testdir/file2 >&    ../outputs/t62

echo ">>>>>>>>running test 63"
../source/allfile.exe -fqr1 <   ../inputs/testdir/file2 >&    ../outputs/t63

echo ">>>>>>>>running test 64"
../source/allfile.exe -fqr2 <   ../inputs/testdir/file2 >&    ../outputs/t64

echo ">>>>>>>>running test 65"
../source/allfile.exe -fqr3 <   ../inputs/testdir/file2 >&    ../outputs/t65

echo ">>>>>>>>running test 66"
../source/allfile.exe -fqr4 <   ../inputs/testdir/file2 >&    ../outputs/t66

echo ">>>>>>>>running test 67"
../source/allfile.exe -fqr5 <   ../inputs/testdir/file2 >&    ../outputs/t67

echo ">>>>>>>>running test 68"
../source/allfile.exe -fqr6 <   ../inputs/testdir/file2 >&    ../outputs/t68

echo ">>>>>>>>running test 69"
../source/allfile.exe -fqr7 <   ../inputs/testdir/file2 >&    ../outputs/t69

echo ">>>>>>>>running test 70"
../source/allfile.exe -fqr8 <   ../inputs/testdir/file2 >&    ../outputs/t70

echo ">>>>>>>>running test 71"
../source/allfile.exe -fqr9 <   ../inputs/testdir/file2 >&    ../outputs/t71

echo ">>>>>>>>running test 72"
../source/allfile.exe -fqr <   ../inputs/testdir/file2 >&    ../outputs/t72

echo ">>>>>>>>running test 73"
../source/allfile.exe -fqv1 <   ../inputs/testdir/file2 >&    ../outputs/t73

echo ">>>>>>>>running test 74"
../source/allfile.exe -fqv2 <   ../inputs/testdir/file2 >&    ../outputs/t74

echo ">>>>>>>>running test 75"
../source/allfile.exe -fqv3 <   ../inputs/testdir/file2 >&    ../outputs/t75

echo ">>>>>>>>running test 76"
../source/allfile.exe -fqv4 <   ../inputs/testdir/file2 >&    ../outputs/t76

echo ">>>>>>>>running test 77"
../source/allfile.exe -fqv5 <   ../inputs/testdir/file2 >&    ../outputs/t77

echo ">>>>>>>>running test 78"
../source/allfile.exe -fqv6 <   ../inputs/testdir/file2 >&    ../outputs/t78

echo ">>>>>>>>running test 79"
../source/allfile.exe -fqv7 <   ../inputs/testdir/file2 >&    ../outputs/t79

echo ">>>>>>>>running test 80"
../source/allfile.exe -fqv8 <   ../inputs/testdir/file2 >&    ../outputs/t80

echo ">>>>>>>>running test 81"
../source/allfile.exe -fqv9 <   ../inputs/testdir/file2 >&    ../outputs/t81

echo ">>>>>>>>running test 82"
../source/allfile.exe -fqv <   ../inputs/testdir/file2 >&    ../outputs/t82

echo ">>>>>>>>running test 83"
../source/allfile.exe -fq1 <   ../inputs/testdir/file2 >&    ../outputs/t83

echo ">>>>>>>>running test 84"
../source/allfile.exe -fq2 <   ../inputs/testdir/file2 >&    ../outputs/t84

echo ">>>>>>>>running test 85"
../source/allfile.exe -fq3 <   ../inputs/testdir/file2 >&    ../outputs/t85

echo ">>>>>>>>running test 86"
../source/allfile.exe -fq4 <   ../inputs/testdir/file2 >&    ../outputs/t86

echo ">>>>>>>>running test 87"
../source/allfile.exe -fq5 <   ../inputs/testdir/file2 >&    ../outputs/t87

echo ">>>>>>>>running test 88"
../source/allfile.exe -fq6 <   ../inputs/testdir/file2 >&    ../outputs/t88

echo ">>>>>>>>running test 89"
../source/allfile.exe -fq7 <   ../inputs/testdir/file2 >&    ../outputs/t89

echo ">>>>>>>>running test 90"
../source/allfile.exe -fq8 <   ../inputs/testdir/file2 >&    ../outputs/t90

echo ">>>>>>>>running test 91"
../source/allfile.exe -fq9 <   ../inputs/testdir/file2 >&    ../outputs/t91

echo ">>>>>>>>running test 92"
../source/allfile.exe -fq <   ../inputs/testdir/file2 >&    ../outputs/t92

echo ">>>>>>>>running test 93"
../source/allfile.exe -frv1 <   ../inputs/testdir/file2 >&    ../outputs/t93

echo ">>>>>>>>running test 94"
../source/allfile.exe -frv2 <   ../inputs/testdir/file2 >&    ../outputs/t94

echo ">>>>>>>>running test 95"
../source/allfile.exe -frv3 <   ../inputs/testdir/file2 >&    ../outputs/t95

echo ">>>>>>>>running test 96"
../source/allfile.exe -frv4 <   ../inputs/testdir/file2 >&    ../outputs/t96

echo ">>>>>>>>running test 97"
../source/allfile.exe -frv5 <   ../inputs/testdir/file2 >&    ../outputs/t97

echo ">>>>>>>>running test 98"
../source/allfile.exe -frv6 <   ../inputs/testdir/file2 >&    ../outputs/t98

echo ">>>>>>>>running test 99"
../source/allfile.exe -frv7 <   ../inputs/testdir/file2 >&    ../outputs/t99

echo ">>>>>>>>running test 100"
../source/allfile.exe -frv8 <   ../inputs/testdir/file2 >&    ../outputs/t100

echo ">>>>>>>>running test 101"
../source/allfile.exe -frv9 <   ../inputs/testdir/file2 >&    ../outputs/t101

echo ">>>>>>>>running test 102"
../source/allfile.exe -frv <   ../inputs/testdir/file2 >&    ../outputs/t102

echo ">>>>>>>>running test 103"
../source/allfile.exe -fr1 <   ../inputs/testdir/file2 >&    ../outputs/t103

echo ">>>>>>>>running test 104"
../source/allfile.exe -fr2 <   ../inputs/testdir/file2 >&    ../outputs/t104

echo ">>>>>>>>running test 105"
../source/allfile.exe -fr3 <   ../inputs/testdir/file2 >&    ../outputs/t105

echo ">>>>>>>>running test 106"
../source/allfile.exe -fr4 <   ../inputs/testdir/file2 >&    ../outputs/t106

echo ">>>>>>>>running test 107"
../source/allfile.exe -fr5 <   ../inputs/testdir/file2 >&    ../outputs/t107

echo ">>>>>>>>running test 108"
../source/allfile.exe -fr6 <   ../inputs/testdir/file2 >&    ../outputs/t108

echo ">>>>>>>>running test 109"
../source/allfile.exe -fr7 <   ../inputs/testdir/file2 >&    ../outputs/t109

echo ">>>>>>>>running test 110"
../source/allfile.exe -fr8 <   ../inputs/testdir/file2 >&    ../outputs/t110

echo ">>>>>>>>running test 111"
../source/allfile.exe -fr9 <   ../inputs/testdir/file2 >&    ../outputs/t111

echo ">>>>>>>>running test 112"
../source/allfile.exe -fr <   ../inputs/testdir/file2 >&    ../outputs/t112

echo ">>>>>>>>running test 113"
../source/allfile.exe -fv1 <   ../inputs/testdir/file2 >&    ../outputs/t113

echo ">>>>>>>>running test 114"
../source/allfile.exe -fv2 <   ../inputs/testdir/file2 >&    ../outputs/t114

echo ">>>>>>>>running test 115"
../source/allfile.exe -fv3 <   ../inputs/testdir/file2 >&    ../outputs/t115

echo ">>>>>>>>running test 116"
../source/allfile.exe -fv4 <   ../inputs/testdir/file2 >&    ../outputs/t116

echo ">>>>>>>>running test 117"
../source/allfile.exe -fv5 <   ../inputs/testdir/file2 >&    ../outputs/t117

echo ">>>>>>>>running test 118"
../source/allfile.exe -fv6 <   ../inputs/testdir/file2 >&    ../outputs/t118

echo ">>>>>>>>running test 119"
../source/allfile.exe -fv7 <   ../inputs/testdir/file2 >&    ../outputs/t119

echo ">>>>>>>>running test 120"
../source/allfile.exe -fv8 <   ../inputs/testdir/file2 >&    ../outputs/t120

echo ">>>>>>>>running test 121"
../source/allfile.exe -fv9 <   ../inputs/testdir/file2 >&    ../outputs/t121

echo ">>>>>>>>running test 122"
../source/allfile.exe -fv <   ../inputs/testdir/file2 >&    ../outputs/t122

echo ">>>>>>>>running test 123"
../source/allfile.exe -f1 <   ../inputs/testdir/file2 >&    ../outputs/t123

echo ">>>>>>>>running test 124"
../source/allfile.exe -f2 <   ../inputs/testdir/file2 >&    ../outputs/t124

echo ">>>>>>>>running test 125"
../source/allfile.exe -f3 <   ../inputs/testdir/file2 >&    ../outputs/t125

echo ">>>>>>>>running test 126"
../source/allfile.exe -f4 <   ../inputs/testdir/file2 >&    ../outputs/t126

echo ">>>>>>>>running test 127"
../source/allfile.exe -f5 <   ../inputs/testdir/file2 >&    ../outputs/t127

echo ">>>>>>>>running test 128"
../source/allfile.exe -f6 <   ../inputs/testdir/file2 >&    ../outputs/t128

echo ">>>>>>>>running test 129"
../source/allfile.exe -f7 <   ../inputs/testdir/file2 >&    ../outputs/t129

echo ">>>>>>>>running test 130"
../source/allfile.exe -f8 <   ../inputs/testdir/file2 >&    ../outputs/t130

echo ">>>>>>>>running test 131"
../source/allfile.exe -f9 <   ../inputs/testdir/file2 >&    ../outputs/t131

echo ">>>>>>>>running test 132"
../source/allfile.exe -f <   ../inputs/testdir/file2 >&    ../outputs/t132

echo ">>>>>>>>running test 133"
../source/allfile.exe -qrv1 <   ../inputs/testdir/file2 >&    ../outputs/t133

echo ">>>>>>>>running test 134"
../source/allfile.exe -qrv2 <   ../inputs/testdir/file2 >&    ../outputs/t134

echo ">>>>>>>>running test 135"
../source/allfile.exe -qrv3 <   ../inputs/testdir/file2 >&    ../outputs/t135

echo ">>>>>>>>running test 136"
../source/allfile.exe -qrv4 <   ../inputs/testdir/file2 >&    ../outputs/t136

echo ">>>>>>>>running test 137"
../source/allfile.exe -qrv5 <   ../inputs/testdir/file2 >&    ../outputs/t137

echo ">>>>>>>>running test 138"
../source/allfile.exe -qrv6 <   ../inputs/testdir/file2 >&    ../outputs/t138

echo ">>>>>>>>running test 139"
../source/allfile.exe -qrv7 <   ../inputs/testdir/file2 >&    ../outputs/t139

echo ">>>>>>>>running test 140"
../source/allfile.exe -qrv8 <   ../inputs/testdir/file2 >&    ../outputs/t140

echo ">>>>>>>>running test 141"
../source/allfile.exe -qrv9 <   ../inputs/testdir/file2 >&    ../outputs/t141

echo ">>>>>>>>running test 142"
../source/allfile.exe -qrv <   ../inputs/testdir/file2 >&    ../outputs/t142

echo ">>>>>>>>running test 143"
../source/allfile.exe -qr1 <   ../inputs/testdir/file2 >&    ../outputs/t143

echo ">>>>>>>>running test 144"
../source/allfile.exe -qr2 <   ../inputs/testdir/file2 >&    ../outputs/t144

echo ">>>>>>>>running test 145"
../source/allfile.exe -qr3 <   ../inputs/testdir/file2 >&    ../outputs/t145

echo ">>>>>>>>running test 146"
../source/allfile.exe -qr4 <   ../inputs/testdir/file2 >&    ../outputs/t146

echo ">>>>>>>>running test 147"
../source/allfile.exe -qr5 <   ../inputs/testdir/file2 >&    ../outputs/t147

echo ">>>>>>>>running test 148"
../source/allfile.exe -qr6 <   ../inputs/testdir/file2 >&    ../outputs/t148

echo ">>>>>>>>running test 149"
../source/allfile.exe -qr7 <   ../inputs/testdir/file2 >&    ../outputs/t149

echo ">>>>>>>>running test 150"
../source/allfile.exe -qr8 <   ../inputs/testdir/file2 >&    ../outputs/t150

echo ">>>>>>>>running test 151"
../source/allfile.exe -qr9 <   ../inputs/testdir/file2 >&    ../outputs/t151

echo ">>>>>>>>running test 152"
../source/allfile.exe -qr <   ../inputs/testdir/file2 >&    ../outputs/t152

echo ">>>>>>>>running test 153"
../source/allfile.exe -qv1 <   ../inputs/testdir/file2 >&    ../outputs/t153

echo ">>>>>>>>running test 154"
../source/allfile.exe -qv2 <   ../inputs/testdir/file2 >&    ../outputs/t154

echo ">>>>>>>>running test 155"
../source/allfile.exe -qv3 <   ../inputs/testdir/file2 >&    ../outputs/t155

echo ">>>>>>>>running test 156"
../source/allfile.exe -qv4 <   ../inputs/testdir/file2 >&    ../outputs/t156

echo ">>>>>>>>running test 157"
../source/allfile.exe -qv5 <   ../inputs/testdir/file2 >&    ../outputs/t157

echo ">>>>>>>>running test 158"
../source/allfile.exe -qv6 <   ../inputs/testdir/file2 >&    ../outputs/t158

echo ">>>>>>>>running test 159"
../source/allfile.exe -qv7 <   ../inputs/testdir/file2 >&    ../outputs/t159

echo ">>>>>>>>running test 160"
../source/allfile.exe -qv8 <   ../inputs/testdir/file2 >&    ../outputs/t160

echo ">>>>>>>>running test 161"
../source/allfile.exe -qv9 <   ../inputs/testdir/file2 >&    ../outputs/t161

echo ">>>>>>>>running test 162"
../source/allfile.exe -qv <   ../inputs/testdir/file2 >&    ../outputs/t162

echo ">>>>>>>>running test 163"
../source/allfile.exe -q1 <   ../inputs/testdir/file2 >&    ../outputs/t163

echo ">>>>>>>>running test 164"
../source/allfile.exe -q2 <   ../inputs/testdir/file2 >&    ../outputs/t164

echo ">>>>>>>>running test 165"
../source/allfile.exe -q3 <   ../inputs/testdir/file2 >&    ../outputs/t165

echo ">>>>>>>>running test 166"
../source/allfile.exe -q4 <   ../inputs/testdir/file2 >&    ../outputs/t166

echo ">>>>>>>>running test 167"
../source/allfile.exe -q5 <   ../inputs/testdir/file2 >&    ../outputs/t167

echo ">>>>>>>>running test 168"
../source/allfile.exe -q6 <   ../inputs/testdir/file2 >&    ../outputs/t168

echo ">>>>>>>>running test 169"
../source/allfile.exe -q7 <   ../inputs/testdir/file2 >&    ../outputs/t169

echo ">>>>>>>>running test 170"
../source/allfile.exe -q8 <   ../inputs/testdir/file2 >&    ../outputs/t170

echo ">>>>>>>>running test 171"
../source/allfile.exe -q9 <   ../inputs/testdir/file2 >&    ../outputs/t171

echo ">>>>>>>>running test 172"
../source/allfile.exe -q <   ../inputs/testdir/file2 >&    ../outputs/t172

echo ">>>>>>>>running test 173"
../source/allfile.exe -rv1 <   ../inputs/testdir/file2 >&    ../outputs/t173

echo ">>>>>>>>running test 174"
../source/allfile.exe -rv2 <   ../inputs/testdir/file2 >&    ../outputs/t174

echo ">>>>>>>>running test 175"
../source/allfile.exe -rv3 <   ../inputs/testdir/file2 >&    ../outputs/t175

echo ">>>>>>>>running test 176"
../source/allfile.exe -rv4 <   ../inputs/testdir/file2 >&    ../outputs/t176

echo ">>>>>>>>running test 177"
../source/allfile.exe -rv5 <   ../inputs/testdir/file2 >&    ../outputs/t177

echo ">>>>>>>>running test 178"
../source/allfile.exe -rv6 <   ../inputs/testdir/file2 >&    ../outputs/t178

echo ">>>>>>>>running test 179"
../source/allfile.exe -rv7 <   ../inputs/testdir/file2 >&    ../outputs/t179

echo ">>>>>>>>running test 180"
../source/allfile.exe -rv8 <   ../inputs/testdir/file2 >&    ../outputs/t180

echo ">>>>>>>>running test 181"
../source/allfile.exe -rv9 <   ../inputs/testdir/file2 >&    ../outputs/t181

echo ">>>>>>>>running test 182"
../source/allfile.exe -rv <   ../inputs/testdir/file2 >&    ../outputs/t182

echo ">>>>>>>>running test 183"
../source/allfile.exe -r1 <   ../inputs/testdir/file2 >&    ../outputs/t183

echo ">>>>>>>>running test 184"
../source/allfile.exe -r2 <   ../inputs/testdir/file2 >&    ../outputs/t184

echo ">>>>>>>>running test 185"
../source/allfile.exe -r3 <   ../inputs/testdir/file2 >&    ../outputs/t185

echo ">>>>>>>>running test 186"
../source/allfile.exe -r4 <   ../inputs/testdir/file2 >&    ../outputs/t186

echo ">>>>>>>>running test 187"
../source/allfile.exe -r5 <   ../inputs/testdir/file2 >&    ../outputs/t187

echo ">>>>>>>>running test 188"
../source/allfile.exe -r6 <   ../inputs/testdir/file2 >&    ../outputs/t188

echo ">>>>>>>>running test 189"
../source/allfile.exe -r7 <   ../inputs/testdir/file2 >&    ../outputs/t189

echo ">>>>>>>>running test 190"
../source/allfile.exe -r8 <   ../inputs/testdir/file2 >&    ../outputs/t190

echo ">>>>>>>>running test 191"
../source/allfile.exe -r9 <   ../inputs/testdir/file2 >&    ../outputs/t191

echo ">>>>>>>>running test 192"
../source/allfile.exe -r <   ../inputs/testdir/file2 >&    ../outputs/t192

echo ">>>>>>>>running test 193"
../source/allfile.exe -v1 <   ../inputs/testdir/file2 >&    ../outputs/t193

echo ">>>>>>>>running test 194"
../source/allfile.exe -v2 <   ../inputs/testdir/file2 >&    ../outputs/t194

echo ">>>>>>>>running test 195"
../source/allfile.exe -v3 <   ../inputs/testdir/file2 >&    ../outputs/t195

echo ">>>>>>>>running test 196"
../source/allfile.exe -v4 <   ../inputs/testdir/file2 >&    ../outputs/t196

echo ">>>>>>>>running test 197"
../source/allfile.exe -v5 <   ../inputs/testdir/file2 >&    ../outputs/t197

echo ">>>>>>>>running test 198"
../source/allfile.exe -v6 <   ../inputs/testdir/file2 >&    ../outputs/t198

echo ">>>>>>>>running test 199"
../source/allfile.exe -v7 <   ../inputs/testdir/file2 >&    ../outputs/t199

echo ">>>>>>>>running test 200"
../source/allfile.exe -v8 <   ../inputs/testdir/file2 >&    ../outputs/t200

echo ">>>>>>>>running test 201"
../source/allfile.exe -v9 <   ../inputs/testdir/file2 >&    ../outputs/t201

echo ">>>>>>>>running test 202"
../source/allfile.exe -v <   ../inputs/testdir/file2 >&    ../outputs/t202

echo ">>>>>>>>running test 203"
../source/allfile.exe -1 <   ../inputs/testdir/file2 >&    ../outputs/t203

echo ">>>>>>>>running test 204"
../source/allfile.exe -2 <   ../inputs/testdir/file2 >&    ../outputs/t204

echo ">>>>>>>>running test 205"
../source/allfile.exe -3 <   ../inputs/testdir/file2 >&    ../outputs/t205

echo ">>>>>>>>running test 206"
../source/allfile.exe -4 <   ../inputs/testdir/file2 >&    ../outputs/t206

echo ">>>>>>>>running test 207"
../source/allfile.exe -5 <   ../inputs/testdir/file2 >&    ../outputs/t207

echo ">>>>>>>>running test 208"
../source/allfile.exe -6 <   ../inputs/testdir/file2 >&    ../outputs/t208

echo ">>>>>>>>running test 209"
../source/allfile.exe -7 <   ../inputs/testdir/file2 >&    ../outputs/t209

echo ">>>>>>>>running test 210"
../source/allfile.exe -8 <   ../inputs/testdir/file2 >&    ../outputs/t210

echo ">>>>>>>>running test 211"
../source/allfile.exe -9 <   ../inputs/testdir/file2 >&    ../outputs/t211

/home/yxb/Documents/gzip/testplans.alt/testscripts/cleanup.sh
