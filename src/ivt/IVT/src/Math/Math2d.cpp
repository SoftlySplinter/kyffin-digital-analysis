// ****************************************************************************
// This file is part of the Integrating Vision Toolkit (IVT).
//
// The IVT is maintained by the Karlsruhe Institute of Technology (KIT)
// (www.kit.edu) in cooperation with the company Keyetech (www.keyetech.de).
//
// Copyright (C) 2012 Karlsruhe Institute of Technology (KIT).
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
//
// 1. Redistributions of source code must retain the above copyright
//    notice, this list of conditions and the following disclaimer.
//
// 2. Redistributions in binary form must reproduce the above copyright
//    notice, this list of conditions and the following disclaimer in the
//    documentation and/or other materials provided with the distribution.
//
// 3. Neither the name of the KIT nor the names of its contributors may be
//    used to endorse or promote products derived from this software
//    without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE KIT AND CONTRIBUTORS “AS IS” AND ANY
// EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
// WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
// DISCLAIMED. IN NO EVENT SHALL THE KIT OR CONTRIBUTORS BE LIABLE FOR ANY
// DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
// (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
// LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
// ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
// THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
// ****************************************************************************
// ****************************************************************************
// Filename:  Math2d.cpp
// Author:    Pedram Azad
// Date:      2005
// ****************************************************************************


// ****************************************************************************
// Includes
// ****************************************************************************

#include <new> // for explicitly using correct new/delete operators on VC DSPs

#include "Math2d.h"
#include "Math3d.h"

#include <math.h>



// ****************************************************************************
// Variables
// ****************************************************************************

const Vec2d Math2d::zero_vec = { 0, 0 };


// ****************************************************************************
// Functions
// ****************************************************************************

void Math2d::SetVec(Vec2d &vec, float x, float y)
{
	vec.x = x;
	vec.y = y;
}

void Math2d::SetVec(Vec2d &vec, const Vec2d &sourceVector)
{
	vec.x = sourceVector.x;
	vec.y = sourceVector.y;
}


void Math2d::AddToVec(Vec2d &vec, const Vec2d &vectorToAdd)
{
	vec.x += vectorToAdd.x;
	vec.y += vectorToAdd.y;
}

void Math2d::SubtractFromVec(Vec2d &vec, const Vec2d &vectorToSubtract)
{
	vec.x -= vectorToSubtract.x;
	vec.y -= vectorToSubtract.y;
}

void Math2d::AddVecVec(const Vec2d &vector1, const Vec2d &vector2, Vec2d &result)
{
	result.x = vector1.x + vector2.x;
	result.y = vector1.y + vector2.y;
}

void Math2d::SetRotationMat(Mat2d &matrix, float theta)
{
	const float s = sinf(theta);
	const float c = cosf(theta);
	
	matrix.r1 = matrix.r4 = c;
	matrix.r2 = -s;
	matrix.r3 = s;
}

void Math2d::MulMatScalar(const Mat2d &matrix, float scalar, Mat2d &result)
{
	result.r1 = matrix.r1 * scalar;
	result.r2 = matrix.r2 * scalar;
	result.r3 = matrix.r3 * scalar;
	result.r4 = matrix.r4 * scalar;
}

void Math2d::MulMatMat(const Mat2d &matrix1, const Mat2d &matrix2, Mat2d &result)
{
	const float r1 = matrix1.r1 * matrix2.r1 + matrix1.r2 * matrix2.r3;
	const float r2 = matrix1.r1 * matrix2.r2 + matrix1.r2 * matrix2.r4;
	const float r3 = matrix1.r3 * matrix2.r1 + matrix1.r4 * matrix2.r3;
	result.r4 = matrix1.r3 * matrix2.r2 + matrix1.r4 * matrix2.r4;
	result.r1 = r1;
	result.r2 = r2;
	result.r3 = r3;
}

void Math2d::MulMatVec(const Mat2d &matrix, const Vec2d &vec, Vec2d &result)
{
	const float temp = matrix.r1 * vec.x + matrix.r2 * vec.y;
	result.y = matrix.r3 * vec.x + matrix.r4 * vec.y;
	result.x = temp;
}

void Math2d::MulMatVec(const Mat2d &matrix, const Vec2d &vector1, const Vec2d &vector2, Vec2d &result)
{
	const float temp = matrix.r1 * vector1.x + matrix.r2 * vector1.y + vector2.x;
	result.y = matrix.r3 * vector1.x + matrix.r4 * vector1.y + vector2.y;
	result.x = temp;
}

void Math2d::MulVecScalar(const Vec2d &vec, float scalar, Vec2d &result)
{
	result.x = scalar * vec.x;
	result.y = scalar * vec.y;
}

void Math2d::SubtractVecVec(const Vec2d &vector1, const Vec2d &vector2, Vec2d &result)
{
	result.x = vector1.x - vector2.x;
	result.y = vector1.y - vector2.y;
}


float Math2d::ScalarProduct(const Vec2d &vector1, const Vec2d &vector2)
{
	return vector1.x * vector2.x + vector1.y * vector2.y;
}

void Math2d::NormalizeVec(Vec2d &vec)
{
	const float length = sqrtf(vec.x * vec.x + vec.y * vec.y);
	
	if (length != 0.0f)
	{
		vec.x /= length;
		vec.y /= length;
	}
}

float Math2d::Length(const Vec2d &vec)
{
	return sqrtf(vec.x * vec.x + vec.y * vec.y);
}

float Math2d::SquaredLength(const Vec2d &vec)
{
	return vec.x * vec.x + vec.y * vec.y;
}

float Math2d::Distance(const Vec2d &vector1, const Vec2d &vector2)
{
	const float x1 = vector1.x - vector2.x;
	const float x2 = vector1.y - vector2.y;

	return sqrtf(x1 * x1 + x2 * x2);
}

float Math2d::SquaredDistance(const Vec2d &vector1, const Vec2d &vector2)
{
	const float x1 = vector1.x - vector2.x;
	const float x2 = vector1.y - vector2.y;

	return x1 * x1 + x2 * x2;
}

float Math2d::Angle(const Vec2d &vector1, const Vec2d &vector2)
{
	const float sp = vector1.x * vector2.x + vector1.y * vector2.y;
	const float l1 = sqrtf(vector1.x * vector1.x + vector1.y * vector1.y);
	const float l2 = sqrtf(vector2.x * vector2.x + vector2.y * vector2.y);

	return acosf(sp / (l1 * l2));
}

void Math2d::RotateVec(const Vec2d &vec, float alpha, Vec2d &result)
{
	const float ca = cosf(alpha);
	const float sa = sinf(alpha);
	
	const float temp = ca * vec.x - sa * vec.y;
	result.y = sa * vec.x + ca * vec.y;
	result.x = temp;
}

void Math2d::Transpose(const Mat2d &matrix, Mat2d &result)
{
	result.r1 = matrix.r1;
	result.r4 = matrix.r4;
	
	const float temp = matrix.r2;
	result.r2 = matrix.r3;
	result.r3 = temp;
}

void Math2d::Invert(const Mat2d &matrix, Mat2d &result)
{
	const float a = matrix.r1;
	const float b = matrix.r2;
	const float c = matrix.r3;
	const float d = matrix.r4;

	float det_inverse = 1 / (a * d - b * c);

	result.r1 = d * det_inverse;
	result.r2 = -b * det_inverse;
	result.r3 = -c * det_inverse;
	result.r4 = a * det_inverse;
}

void Math2d::ApplyHomography(const Mat3d &A, const Vec2d &p, Vec2d &result)
{
	// optimized version of:
	// (x', y', z') = A * (p.x, p.y, 1)^T
	// x = x' / z'
	// y = y' / z'
	
	const float y_ = A.r4 * p.x + A.r5 * p.y + A.r6;
	const float z_ = A.r7 * p.x + A.r8 * p.y + A.r9;
		
	result.x = (A.r1 * p.x + A.r2 * p.y + A.r3) / z_;
	result.y = y_ / z_;
}
