/*
 * Copyright (c) 2015-2025, Wood
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without modification,
 * are permitted provided that the following conditions are met:
 *
 *     * Redistributions of source code must retain the above copyright notice,
 *       this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright notice,
 *       this list of conditions and the following disclaimer in the documentation
 *       and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
 * OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 */

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

#define MX (((z >> 5 ^ y << 2) + (y >> 3 ^ z << 4)) ^ ((sum ^ y) + (k[(p & 3) ^ e] ^ z)))

typedef uint8_t byte;
typedef uint32_t uint;

static uint* bytes2long(const char* s, int dataLen, int* arrLen, int littleEndian, int fill) {
    uint i, count, count2;
    const byte* buff = (const byte*)s;
    byte* tmp = NULL;
    count = dataLen / 4;
    count2 = dataLen % 4;
    if (count2 != 0) {
        count += 1;
        if (fill <= 0) {
            fill = count * 4;
        } else {
            count = fill / 4;
        }
    }
    *arrLen = count;
    uint* dst = (uint*)malloc(count * sizeof(uint));
    if (!dst) {
        if (tmp) free(tmp);
        return NULL;
    }
    if (fill > 0) {
        tmp = (byte*)malloc(fill);
        if (!tmp) {
            free(dst);
            return NULL;
        }
        if (dataLen >= fill) {
            memcpy(tmp, s, fill);
        } else {
            memcpy(tmp, s, dataLen);
            memset(tmp + dataLen, 0, fill - dataLen);
        }
        buff = tmp;
        count = fill / 4;
    }
    if (littleEndian) {
        for (i = 0; i < count; i++) {
            dst[i] = (uint)buff[i*4] | ((uint)buff[i*4 + 1] << 8) | ((uint)buff[i*4 + 2] << 16) | ((uint)buff[i*4 + 3] << 24);
        }
    } else {
        for (i = 0; i < count; i++) {
            dst[i] = ((uint)buff[i*4] << 24) | ((uint)buff[i*4 + 1] << 16) | ((uint)buff[i*4 + 2] << 8) | (uint)buff[i*4 + 3];
        }
    }
    if (tmp) free(tmp);
    return dst;
}

static PyObject* long2bytes(uint* dst, int length, int littleEndian, int cut) {
    int i;
    uint u;
    size_t cutLen = length << 2;
    if (cut) {
        cutLen = (length - 1) << 2;
        size_t newLen = dst[length - 1];
        if ((newLen < cutLen - 3) || (newLen > cutLen)) {
            Py_RETURN_NONE;
        }
        cutLen = newLen;
    }
    byte* rBytes = (byte*)malloc(length * 4);
    if (!rBytes) {
        free(rBytes);
        Py_RETURN_NONE;
    }
    if (littleEndian) {
        for (i = 0; i < length; i++) {
            u = dst[i];
            rBytes[i*4] = (byte)u;
            rBytes[i*4 + 1] = (byte)(u >> 8);
            rBytes[i*4 + 2] = (byte)(u >> 16);
            rBytes[i*4 + 3] = (byte)(u >> 24);
        }
    } else {
        for (i = 0; i < length; i++) {
            u = dst[i];
            rBytes[i*4] = (byte)(u >> 24);
            rBytes[i*4 + 1] = (byte)(u >> 16);
            rBytes[i*4 + 2] = (byte)(u >> 8);
            rBytes[i*4 + 3] = (byte)u;
        }
    }
    PyObject* result = PyBytes_FromStringAndSize((const char*)rBytes, cutLen);
    if (!result) Py_RETURN_NONE;
    free(rBytes);
    return result;
}

static PyObject* decrypt(PyObject* self, PyObject* args) {
    const char *dataBuff, *signBuff, *keyBuff;
    Py_ssize_t dLen, sLen, kLen;
    uint y, z, sum;
    int p, e, vLen, kLen2, n, q;
    uint* v = NULL;
    uint* k = NULL; 
    uint _DELTA = 0x9e3779b9;
    int cut = 1;
    int inputLittleEndian = 1;
    int outputLittleEndian = 1;

    PyObject *result = NULL;

    if (!PyArg_ParseTuple(args, "y#y#y#|Iiii", 
                          &dataBuff, &dLen, 
                          &signBuff, &sLen, 
                          &keyBuff, &kLen, 
                          &_DELTA, &cut,
                          &inputLittleEndian, &outputLittleEndian))
        return NULL;
    printf("dataBuff length: %ld\n", (long)dLen);
    printf("signBuff length: %ld\n", (long)sLen);
    printf("keyBuff length: %ld\n", (long)kLen);
    printf("_DELTA: %u\n", _DELTA);
    printf("cut: %s\n", cut ? "True" : "False");
    printf("inputLittleEndian: %s\n", inputLittleEndian ? "True" : "False");
    printf("outputLittleEndian: %s\n", outputLittleEndian ? "True" : "False");
	fflush(stdout);

    if (dLen == 0) {
        result = PyBytes_FromStringAndSize("", 0);
        goto cleanup;
    }

    if (sLen > 0 && (dLen < sLen || memcmp(dataBuff, signBuff, sLen) != 0)) {
        result = PyBytes_FromStringAndSize("", 0);
        goto cleanup;
    }

    v = bytes2long(dataBuff + sLen, dLen - sLen, &vLen, inputLittleEndian, 0);
    if (!v) {
        result = PyBytes_FromStringAndSize("", 0);
        goto cleanup;
    }

    k = bytes2long(keyBuff, kLen, &kLen2, inputLittleEndian, 16);
    if (!k) {
        result = PyBytes_FromStringAndSize("", 0);
        goto cleanup;
    }

    n = vLen - 1;
    y = v[0];
    q = 6 + 52 / (n + 1);
    sum = q * _DELTA;

    do {
        e = (sum >> 2) & 3;
        for (p = n; p > 0; p--) {
            z = v[p - 1];
            v[p] -= MX;
            y = v[p];
        }
        z = v[n];
        v[0] -= MX;
        y = v[0];
        sum -= _DELTA;
    } while (--q);

    result = long2bytes(v, vLen, outputLittleEndian, cut);

cleanup:
    if (v) free(v);
    if (k) free(k);

    return result;
}

static PyMethodDef CxxteaMethods[] = {
    {"decrypt", (PyCFunction)decrypt, METH_VARARGS, "Decrypt XXTEA"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef cxxteamodule = {
    PyModuleDef_HEAD_INIT,
    "cxxtea",
    NULL,
    -1,
    CxxteaMethods
};

PyMODINIT_FUNC PyInit_cxxtea(void) {
    return PyModule_Create(&cxxteamodule);
}
