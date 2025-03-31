#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2025/03/31 11:07:38
# @Author  : Deming Li
# @Email   : 416587111@qq.com
# @File    : server.py

from contextlib import asynccontextmanager
from dataclasses import dataclass
from dotenv import load_dotenv
import os
import jenkins
import asyncio

from mcp.server.fastmcp import Context, FastMCP

mcp = FastMCP("Mcp Jenkins Server", log_level="ERROR")


@dataclass
class JenkinsContext:
    client: jenkins.Jenkins


@asynccontextmanager
async def app_lifespan(server: FastMCP):
    """Manage application lifecycle with type-safe context"""
    # Initialize on startup
    load_dotenv()
    jenkins_url = os.getenv('JENKINS_URL')
    jenkins_user = os.getenv('JENKINS_USER')
    jenkins_token = os.getenv('JENKINS_TOKEN')

    client = await asyncio.to_thread(
        jenkins.Jenkins,
        jenkins_url,
        username=jenkins_user,
        password=jenkins_token
    )
    try:
        yield JenkinsContext(client=client)
    finally:
        pass

mcp = FastMCP("Mcp Jenkins Server", lifespan=app_lifespan, log_level="ERROR")


@mcp.tool()
def get_jenkins_info(ctx: Context):
    """Get Jenkins info"""
    client = ctx.request_context.lifespan_context.client
    return client.get_info()


@mcp.tool()
def list_jobs(ctx: Context):
    """List all Jenkins jobs"""
    client = ctx.request_context.lifespan_context.client
    return client.get_jobs()


@mcp.tool()
def get_job_info(ctx: Context, job_name: str):
    """Get Jenkins job info"""
    client = ctx.request_context.lifespan_context.client
    return client.get_job_info(job_name)


@mcp.tool()
def get_build_info(ctx: Context, job_name: str, build_number: int):
    """Get Jenkins build info"""
    client = ctx.request_context.lifespan_context.client
    return client.get_build_info(job_name, build_number)


@mcp.tool()
def get_build_console_output(ctx: Context, job_name: str, build_number: int):
    """Get Jenkins build console output"""
    client = ctx.request_context.lifespan_context.client
    return client.get_build_console_output(job_name, build_number)


@mcp.tool()
def get_views(ctx: Context):
    """Get Jenkins views"""
    client = ctx.request_context.lifespan_context.client
    return client.get_views()


@mcp.tool()
def trriger_llm_demo_job_build(ctx: Context, user: str):
    """Trigger job llm demo build"""
    client = ctx.request_context.lifespan_context.client
    parameters = {
        'user': user
    }
    return client.build_job('LLM_Demo', parameters=parameters)


if __name__ == "__main__":
    mcp.run()
